from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import *

app_name = "shop"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='shop/login_page.html'), name='login'),
    path('', views.product_main, name='main'),
    path('login/signup/', views.signup, name='signup'),
]