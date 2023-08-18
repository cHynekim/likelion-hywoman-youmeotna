
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from accounts import models
from accounts.forms import AccountAuthForm, RegistrationForm
import sys

from accounts.models import Account
from comment.models import Comment

sys.setrecursionlimit(9999)

def signUp(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("이미" +str(user.phonenum)+ "으로 로그인이 되어있습니다.")

    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            raw_phonenum = form.cleaned_data.get('phonenum')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(phonenum=raw_phonenum, password=raw_password)

            if account is not None:
                login(request, account)
            form.save()
            return redirect('shop:main')
        # else:
        #     context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'accounts/signUp.html', context)

def login(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("shop:main")

    destination = get_redirect_if_exists(request)

    if request.POST:
        form = AccountAuthForm(request.POST)
        if form.is_valid():
            phonenum = request.POST.get('phonenum')
            password = request.POST.get('password')
            user = authenticate(phonenum=phonenum, password=password)
            if user:
                login(request, user)
                if destination:
                    return redirect(destination, "shop:main")
                return redirect("shop:main")
    else:
        form = AccountAuthForm()

    context['login_form'] = form
    return render(request, "accounts/login_page.html", context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect

def custom_logout(request):
    print('Logout {}'.format(request.user))
    logout(request)
    print(request.user)
    return redirect('accounts/login_page.html')

@login_required
def userinfo(request, pk):
    user = request.user
    profile = Account.objects.get(pk=request.user.pk)
    

    user_comments = Comment.objects.filter(user=request.user)


    context = {
        'id' : user.phonenum,
        'nick' : profile.nickname,
        'birthY' : profile.birthY,
        'birthM' : profile.birthM,
        'birthD' : profile.birthD,
        'user' : user,
        'user_comments': user_comments,
    }
    return render(request, 'accounts/setting2.html', context=context)
