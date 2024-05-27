from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('core.urls', namespace='core')),
    path('shop/', include('shop.urls', namespace='shop')),
]
