from django.urls import path

from .views import *

app_name = "shop"

urlpatterns = [
    path('', main, name='main'),
    # path('<product-slug>/<int:id>', detail, name='detail'),
    path('detail/', detail_view, name='detail2'), #임시입니다..
]