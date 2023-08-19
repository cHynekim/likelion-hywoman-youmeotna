from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', detail, name='cart'), # 장바구니 페이지
    path('add/<int:product_id>', product_add, name='product_add'), # 추가
    path('remove/<int:product_id>', remove, name='remove'), # 삭제
    path('clear/', clear, name='clear'), # 비우기
    path('order/', order_start, name='order'),
]