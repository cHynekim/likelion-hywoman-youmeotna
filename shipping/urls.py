from django.urls import path
from . import views

app_name = 'shipping'

urlpatterns = [
    path('shipping/', views.shipping, name='shipping'),
]