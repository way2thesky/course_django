from django.db.models import Avg, Max, Min
from django.views.generic import DetailView, ListView
from .models import Author, Book, Publisher, Store
from django.shortcuts import render
from django.views import generic


def index(request):
    """ Функция отображения для домашней страницы сайта"""
    return render(request, 'index.html')


class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'


class BookListView(generic.ListView):
    model = Book
    template_name = 'library/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'

    # queryset = Book.objects.all().select_related('publisher').prefetch_related('stores')
    # average_price = Book.objects.aggregate(average_price=Avg('price'))


class PublisherListView(ListView):
    model = Publisher
    template_name = 'library/publisher_list.html'


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'library/publisher_detail.html'


class StoreListView(ListView):
    model = Store
    template_name = 'library/store_list.html'


class StoreDetailView(DetailView):
    model = Store
    template_name = 'library/store_detail.html'
