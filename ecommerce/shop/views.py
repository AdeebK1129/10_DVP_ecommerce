from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Favorite, Product, CartItem, Order
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import pandas as pd 
import io
import base64
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import json
from django.conf import settings
from django.utils import timezone
class ProductShowView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        products = Product.objects.values('category', 'price')
        df_products = pd.DataFrame(list(products))
        product_price = product.price
        product_category = product.category
        
        category_avg_price = df_products[df_products['category'] == product_category]['price'].mean()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(['This Product', 'Category Average'], [product_price, category_avg_price])
        ax.set_title(f'Price Comparison with other products in this category')

        
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')

        
        return render(request, 'shop/product_show.html', {'product_id': product_id, 'plot_data': plot_data})

class ProductShowJsonView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        product_data = {
            'id': product.id,
            'title': product.title,
            'price': product.price,
            'category': product.category,
            'description': product.description,
            'image': product.image,
        }
        return JsonResponse({'product': product_data})

@method_decorator(login_required, name='dispatch')
class AddFavoriteView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
        if created:
            return JsonResponse({'message': 'Added to favorites'})
        return HttpResponseBadRequest('Already in favorites')

@method_decorator(login_required, name='dispatch')
class RemoveFavoriteView(View):
    def post(self, request, product_id):
        favorite = get_object_or_404(Favorite, user=request.user, product_id=product_id)
        favorite.delete()
        return redirect('shop:user_favorites')

@method_decorator(login_required, name='dispatch')
class UserFavoritesView(View):
    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user).select_related('product')
        return render(request, 'shop/favorites.html', {'favorites': favorites})

@login_required
def fetch_favorites(request):
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user).values('product__id', 'product__title', 'product__price')
        return JsonResponse({'favorites': list(favorites)})
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    

@csrf_exempt
@require_POST
def AddToCart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    try:
        data = json.loads(request.body)
        quantity = data.get('quantity', 1)
        quantity = int(quantity)
        if quantity < 1:
            quantity = 1  # Ensure quantity is at least 1
    except (ValueError, TypeError, KeyError, json.JSONDecodeError):
        return JsonResponse({'success': False, 'error': 'Invalid quantity'}, status=400)
    
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=product,
        defaults={'quantity': quantity}
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    return JsonResponse({'success': True})


@method_decorator(login_required, name='dispatch')
class RemoveFromCart(View):
    def post(self, request, product_id):
        item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
        item.delete()
        return redirect('shop:user_cart')

@method_decorator(login_required, name='dispatch')
class UserCartView(View):
    def get(self, request):
        carts = CartItem.objects.filter(user=request.user).select_related('product')
        return render(request, 'shop/cart.html', {'carts': carts})

@login_required
def fetch_cart(request):
    if request.user.is_authenticated:
        carts = CartItem.objects.filter(user=request.user).values('product__id', 'product__title', 'product__price')
        return JsonResponse({'carts': list(carts)})
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

@login_required

def checkout_view(request):
    carts = CartItem.objects.filter(user=request.user)
    total_price = sum(cart.product.price * cart.quantity for cart in carts)
    context = {
        'carts': carts,
        'total_price': total_price,
        'paypal_client_id': settings.PAYPAL_CLIENT_ID,
    }
    return render(request, 'shop/checkout.html', context)

def create_order(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        order_id = body['orderID']
        
        carts = CartItem.objects.filter(user=request.user)
        product_names = ", ".join([cart.product.title for cart in carts])
        
        order = Order.objects.create(
            user=request.user,
            order_date=timezone.now(),
            products=product_names,
        )
        
        carts.delete()
        
        return JsonResponse({'order_id': order.id})

def payment_successful(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'shop/payment_success.html', {'order': order})

def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': list(orders.values('id', 'order_date', 'products')),
    }
    return render(request, 'shop/orders.html', context)

def cancel_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, id=order_id, user=request.user)
        order.delete()
        return redirect('shop:orders')