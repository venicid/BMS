from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth  # auth认证模块
from django.contrib.auth.models import User  # auth_user表对象
from login_reg.loginforms import UserForm   # 导入loginforms组件
from log import mylog  # log日志

logger = mylog.log_handle('login_reg')


def index(request):
    """输入网址,网站首页"""
    logger.info("进入 [login_reg:index]")
    return render(request, './login_reg/index.html')


def reg(request):
    """注册"""
    logger.info("进入 [login_reg:reg]")
    if request.method == "POST":
        form = UserForm(request.POST)
        username = request.POST.get("username")
        if form.is_valid():
            # username = form.cleaned_data.get('username')  # <QuerySet []>？
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(username=username, password=password, email=email)
            logger.info("[用户%s注册成功]" % username)
            next_url = reverse('login_reg:login')
            return redirect(next_url)
        else:
            logger.error("[用户%s注册失败]" % username)
            errors = form.errors.get("__all__")
            return render(request, './login_reg/reg.html', locals())

    form = UserForm()
    return render(request, './login_reg/reg.html', locals())


def login(request):
    """登录"""
    logger.info("进入 [login_reg:login]")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 用户是否通过认证
        auth_user = auth.authenticate(username=username, password=password)
        if auth_user:
            auth.login(request, auth_user)    # request.user == username
            logger.info("[用户%s登录成功]" % username)
            next_url = reverse('book:index')
            return redirect(next_url, locals())
        else:
            logger.error("[用户%s登录失败]" % username)
            error_msg = 'Error username or password'
            return render(request, "./login_reg/login.html", locals())

    return render(request, "./login_reg/login.html", locals())


def logout(request):
    """登出"""
    logger.info("进入 [login_reg:logout]")
    logger.info("[用户%s退出]" % request.user.username)

    auth.logout(request)
    next_url = reverse('login_reg:index')

    return redirect(next_url)


def error(request):
    """404页面"""
    logger.error("[login_reg:error] 出现404")
    return render(request, 'login_reg/404.html')
