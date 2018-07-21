
from django.urls import path, re_path, include
from book import views
urlpatterns = [
    re_path('^index/$', views.index, name='index'),

    # 图书list, add, edit, delete
    re_path('^book_list/$', views.book_list, name='book_list'),
    re_path('^add_book/$', views.add_book, name='add_book'),
    re_path('^edit_book/(\d+)/$', views.edit_book, name='edit_book'),
    re_path('^delete_book/(\d+)/$', views.delete_book, name='delete_book'),

    # author list, add, edit, delete
    re_path('^author_list/$', views.author_list, name='author_list'),
    re_path('^author2book/(\d+)/$', views.author2book, name='author2book'),
    re_path('^add_author/$', views.add_author, name='add_author'),
    re_path('^edit_author/(\d+)/$', views.edit_author, name='edit_author'),
    re_path('^delete_author/(\d+)/$', views.delete_author, name='delete_author'),

    # publish list, add, edit, delete
    re_path('^publish_list/$', views.publish_list, name='publish_list'),
    re_path('^publish2book/(\d+)/$', views.publish2book, name='publish2book'),
    re_path('^add_publish/$', views.add_publish, name='add_publish'),
    re_path('^edit_publish/(\d+)/$', views.edit_publish, name='edit_publish'),
    re_path('^delete_publish/(\d+)/$', views.delete_publish, name='delete_publish'),

    # 404
    # re_path(r'^.*/$', views.error, name='error'),
]
