"""
index 主页
reg  注册
login   登录
logout  登出
"""

from django.urls import path, re_path, include
from login_reg import views
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^reg/$', views.reg, name='reg'),
    re_path(r'^logout/$', views.logout, name='logout'),
    # 404
    # re_path(r'^.*/$', views.error, name='error'),
]
