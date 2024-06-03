from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Favorite, Product
import pandas as pd 
import io
import base64
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import json

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
        return JsonResponse({'message': 'Removed from favorites'})

@method_decorator(login_required, name='dispatch')
class UserFavoritesView(View):
    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user).select_related('product')
        return render(request, 'shop/favorites.html', {'favorites': favorites})
