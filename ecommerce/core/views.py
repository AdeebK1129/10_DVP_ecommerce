from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://fakestoreapi.com/products/categories')
    categories = response.json()
    return render(request, 'core/home.html', {'categories': categories})

def category_products(request, category_name):
    response = requests.get(f'https://fakestoreapi.com/products/category/{category_name}')
    products = response.json()
    return render(request, 'core/category_products.html', {'products': products, 'category_name': category_name})

