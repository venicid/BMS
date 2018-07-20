from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth  # auth认证模块
from django.contrib.auth.models import User  # auth_user表对象
from login_reg.loginforms import UserForm   # 导入loginforms组件


def index(request):
    """输入网址,网站首页"""

    return render(request, './login_reg/index.html')


def reg(request):
    """注册"""
    if request.method == "POST":
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            next_url = reverse('login_reg:login')
            return redirect(next_url)
        else:
            errors = form.errors.get("__all__")
            return render(request, './login_reg/reg.html', locals())

    form = UserForm()
    return render(request, './login_reg/reg.html', locals())


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
        else:
            error_msg = 'Error username or password'

    return render(request, "./login_reg/login.html", locals())


def logout(request):
    """登出"""
    auth.logout(request)
    next_url = reverse('login_reg:index')

    return redirect(next_url)

