
from django.urls import path, re_path, include
from book import views
urlpatterns = [
    re_path('^index/$', views.index, name='index'),
    re_path('^book_list/$', views.book_list, name='book_list'),
    re_path('^add_book/$', views.add_book, name='add_book'),
    re_path('^add_book_success/$', views.add_book_success, name='add_book_success'),
    # re_path('^edit_book/(\d+)/$', views.edit_book, name='edit_book'),
    # re_path('^delete_book/(\d+)/$', views.delete_book, name='delete_book'),
]
