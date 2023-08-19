from django.contrib.auth import authenticate, login
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from comment.models import Comment
from .models import *
from cart.forms import AddCartForm

# Create your views here.
# 상품 메인 (전체 상품)
def main(request):
    products = Product.objects.filter(available_display=True)
    return render(request, 'shop/main.html', {'products':products})

# 상품 상세 -> 장바구니 구현 후 장바구니 담기 추가
def detail_view(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)

    # 장바구니 담기 기능 활성화를 위해 뷰 슈정
    add_to_cart = AddCartForm(initial={'quantity':1})
    return render(request, 'shop/detail.html', {'product':product, 'add_to_cart':add_to_cart, 'comments':comments})

#임시 detail(with 평균 별점 계산)
def detail(request, product_id, product_slug=None):
    # 모든 사용자의 댓글 별점 조회..
    all_ratings = Comment.objects.filter(rating__isnull=False).values_list('rating', flat=True)

    #  추가1 -> 위 뷰 합함
    product = get_object_or_404(Product, id=product_id, slug=product_slug)

    # 별점의 평균 계산
    if all_ratings:
        average_rating = sum(all_ratings) / len(all_ratings)
    else:
        average_rating = 0

    add_to_cart = AddCartForm(initial={'quantity': 1})

    context = {
        'average_rating': average_rating,
        'product': product,
        'add_to_cart': add_to_cart,
    }

    return render(request, 'shop/detail.html', context)


