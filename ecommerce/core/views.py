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


url = "https://unofficial-shein.p.rapidapi.com/auto-complete"

querystring = {"word":"bikini top","language":"en","country":"US","currency":"USD"}

headers = {
	"X-RapidAPI-Key": "e64bc78181msh84af989eb88db6bp175393jsnb6a8429b02ed",
	"X-RapidAPI-Host": "unofficial-shein.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)




