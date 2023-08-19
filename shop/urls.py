from django.urls import path, include

from .views import *

app_name = "shop"

urlpatterns = [
    path('', main, name='main'),
    # path('<int:id>/<product_slug>/', detail, name='detail),
    path('<int:product_id>/<product_slug>/', detail, name='detail'),
]