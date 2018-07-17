
from django.urls import path, re_path, include
from book import views
urlpatterns = [
    re_path('^index/$', views.index, name='index'),
]
