from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from comment.forms import CommentForm
from comment.models import Comment
from shipping.models import Shipping
from shop.models import Product


# Create your views here.

#댓글 달기
@login_required
def create_comment(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.product = product
            comment.save()
            return redirect('shipping:shipping')
    else:
        form = CommentForm()

    context = {
        'form': form,
        'product_id': product_id,
        'product': product,
    }

    return render(request, 'comment/comment.html', context)

#평균 별점 계산
def detail_view(request):
    # 모든 사용자의 댓글 별점 조회..
    all_ratings = Comment.objects.filter(rating__isnull=False).values_list('rating', flat=True)

    # 별점의 평균 계산
    if all_ratings:
        average_rating = sum(all_ratings) / len(all_ratings)
    else:
        average_rating = 0

    context = {
        'average_rating': average_rating,
    }

    return render(request, 'shop/detail.html', context)

#상품 댓글
def product_comments(request, product_id):
    product = Product.objects.get(id=product_id)
    comments = Comment.objects.filter(product_id=product)

    context = {
        'product': product,
        'comments': comments,
    }

    return render(request, 'shop/detail.html', context=context)

#수정
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment.text = request.POST['text']
        comment.rating = int(request.POST['rating'])
        comment.save()
        return redirect('accounts:userinfo', pk=comment.user.id)

    context = {'comment': comment}
    return render(request, 'comment/edit_comment.html', context)