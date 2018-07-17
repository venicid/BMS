from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth  # auth认证模块
from django.contrib.auth.models import User  # auth_user表对象


def index(request):
    """输入网址,网站首页"""

    return render(request, './login_reg/index.html')


def reg(request):
    """注册"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # r_password = request.POST.get("r_password")
        email = request.POST.get("email")
        user_obj = User.objects.create_user(username=username, password=password, email=email)

        next_url = reverse('login_reg:login')
        return redirect(next_url)

    return render(request, './login_reg/reg.html')


def login(request):
    """登录"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 用户是否通过认证
        auth_user = auth.authenticate(username=username, password=password)
        if auth_user:
            auth.login(request, auth_user)    # request.user == username
            next_url = reverse('book:index')
            return redirect(next_url, locals())

    return render(request, "./login_reg/login.html")


def logout(request):
    """登出"""
    auth.logout(request)
    next_url = reverse('login_reg:index')

    return redirect(next_url)

