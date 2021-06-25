from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('publisher/', views.PublisherListView.as_view(), name='publisher_list'),
    path('store/', views.StoreListView.as_view(), name='store_list'),
]
