from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Favorite
import requests
import json

class ProductShowView(View):
    def get(self, request, product_id):
        response = requests.get(f'https://fakestoreapi.com/products/{product_id}')
        product = response.json()
        return render(request, 'shop/product_show.html', {'product_id': product_id})

class ProductShowJsonView(View):
    def get(self, request, product_id):
        response = requests.get(f'https://fakestoreapi.com/products/{product_id}')
        product = response.json()
        return JsonResponse({'product': product})

@method_decorator(login_required, name='dispatch')
class AddFavoriteView(View):
    def post(self, request, product_id):
        product_name = json.loads(request.body).get('product_name')
        favorite, created = Favorite.objects.get_or_create(user=request.user, product_id=product_id, product_name=product_name)
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
        favorites = Favorite.objects.filter(user=request.user)
        return render(request, 'shop/favorites.html', {'favorites': favorites})
