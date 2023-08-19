from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "accounts"

urlpatterns = [
    #path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login_page.html'), name='login'),
    path('signup/', views.signUp, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/login_page.html'), name='logout'),
    path('userinfo/<int:pk>/', views.userinfo, name='userinfo'),
]