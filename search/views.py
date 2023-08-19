from django.http import JsonResponse
from django.shortcuts import render, redirect

from search.models import SearchHistory
from shop.models import Product
from django.db.models import Q, Count


# Create your views here.
def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))

        if request.user.is_authenticated:  # 로그인한 사용자인 경우에만 기록...
            SearchHistory.objects.create(user=request.user, query=query)
            request.session['search_results'] = list(products.values('id', 'slug'))

    return render(request, 'shop/product_list_page.html', {'query':query, 'products':products})

def searchResult(request):
    products = None
    query = None
    sort = request.GET.get('sort')  # 정렬 옵션 가져오기
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))

        if sort == 'popularity':
            products = products.annotate(num_comments=Count('comment', filter=Q(comment__rating__isnull=False))).order_by('-num_comments')
        elif sort == 'fastest':
            products = products.order_by('delivery_date')
        elif sort == 'cheap':
            products = products.order_by('price')

        if request.user.is_authenticated:
            SearchHistory.objects.create(user=request.user, query=query)
            request.session['search_results'] = list(products.values('id', 'slug'))

    return render(request, 'shop/product_list_page.html', {'query': query, 'products': products})

def clear_search_history(request):
    if request.user.is_authenticated:
        request.user.searchhistory_set.all().delete()