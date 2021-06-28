from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),

    path('books/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    path('publishers/', views.PublisherListView.as_view(), name='publisher-list'),
    path('publisher/<int:pk>', views.PublisherDetailView.as_view(), name='publisher-detail'),

    path('stores/', views.StoreListView.as_view(), name='store-list'),
    path('store/<int:pk>', views.StoreDetailView.as_view(), name='store-detail'),
]
