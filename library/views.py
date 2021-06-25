from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from .models import Author, Book, Publisher, Store


class BookListView(ListView):
    model = Book
    paginate_by = 1000
    template_name = 'library/book_list.html'
    queryset = Book.objects.all().prefetch_related('authors__book_set').all()
    ordering = ['name']


class BookDetailView(DetailView):
    model = Book
    paginate_by = 10
    template_name = 'library/author_detail.html'
    ordering = ['name']


class AuthorListView(ListView):
    model = Author
    paginate_by = 10
    template_name = 'library/author_list.html'
    ordering = ['name']


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'


class PublisherListView(ListView):
    model = Publisher
    paginate_by = 10
    template_name = 'library/publisher_list.html'
    ordering = ['name']


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'library/publisher_detail.html'


class StoreListView(ListView):
    model = Store
    paginate_by = 10
    template_name = 'library/store_list.html'
    ordering = ['name']


class StoreDetailView(DetailView):
    model = Store
    template_name = 'library/store_detail.html'
