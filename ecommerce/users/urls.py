from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  
]