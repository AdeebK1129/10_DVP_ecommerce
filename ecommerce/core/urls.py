from django.urls import path, include
from .views import home, category_products

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),  
    path('category/<str:category_name>/', category_products, name='category'),
]