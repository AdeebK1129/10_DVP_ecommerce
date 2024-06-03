from django.urls import path
from .views import ProductShowView, ProductShowJsonView, AddFavoriteView, RemoveFavoriteView, UserFavoritesView

app_name = 'shop'

urlpatterns = [
    path('product/<int:product_id>/', ProductShowView.as_view(), name='product_show'),
    path('product/<int:product_id>/json/', ProductShowJsonView.as_view(), name='product_show_json'),
    path('favorites/add/<int:product_id>/', AddFavoriteView.as_view(), name='add_to_favorites'),
    path('favorites/remove/<int:product_id>/', RemoveFavoriteView.as_view(), name='remove_from_favorites'),
    path('favorites/', UserFavoritesView.as_view(), name='user_favorites'),
]
