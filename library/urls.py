from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('authors/', views.AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),

    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),

    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),

    path('stores/', views.StoreList.as_view(), name='store-list'),
    path('store/<int:pk>/', views.StoreDetail.as_view(), name='store-detail'),
]
