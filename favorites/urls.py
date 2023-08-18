from django.urls import path
from . import views

app_name='favorites'

urlpatterns = [
    path('favorites/', views.favorite_products, name='favorite_products'),
    path('<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('search/<int:product_id>/', views.list_favorite, name='list_favorite'),
]