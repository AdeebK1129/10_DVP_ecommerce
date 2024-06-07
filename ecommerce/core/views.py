from django.shortcuts import render
from shop.models import Product
import pandas as pd 
import io
import base64
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import requests

def home(request):
    response = requests.get('https://fakestoreapi.com/products/categories')
    categories = response.json()
    print(categories)
    products = Product.objects.values('category', 'price')
    print(products)
    df_products = pd.DataFrame(list(products))

    
    categorygroup = df_products.groupby('category')

    avgpricecategory = categorygroup['price'].mean()
    avgpricecategory = avgpricecategory.reset_index()

    avgpricecategory.plot(kind='bar', x='category', y='price', figsize=(10, 6))

    plt.xlabel('Category')
    plt.ylabel('Average Price')
    plt.title('Average Price by Category')
    plt.xticks(rotation = 0)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render(request, 'core/home.html', {'categories': categories, 'plot_data' : plot_data})


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




