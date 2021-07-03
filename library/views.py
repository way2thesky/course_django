from django.contrib.auth import get_user_model
from django.db.models import Avg, Count, Max, Min, Sum
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from .models import Author, Book, Publisher, Store

User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'index.html'


class AuthorList(ListView):
    model = Author
    template_name = 'library/author_list.html'
    context_object_name = 'authors'
    queryset = Author.objects.prefetch_related('book_set__authors')


class AuthorDetail(DetailView):
    model = Author
    template_name = 'library/author_detail.html'
    context_object_name = 'author'


class BookList(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    queryset = Book.objects.annotate(num_authors=Count('authors'))

    def get_queryset(self, **kwargs):
        return super(BookList, self).get_queryset() \
            .select_related('publisher') \
            .prefetch_related('authors__book_set').all()


class BookDetail(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'
    Book.objects.select_related('publisher').prefetch_related('authors')


def get_context_data(self, **kwargs):
    context = super(BookDetail, self).get_context_data(**kwargs)
    context['book_total'] = Book.objects.filter(pk=self.kwargs.get('pk')).aggregate(
        book_total=Sum('price') + Sum('price')
    )
    return context


class PublisherList(ListView):
    model = Publisher
    template_name = 'library/publisher_list.html'
    context_object_name = 'publishers'
    queryset = Publisher.objects.prefetch_related('book_set__authors')


class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'library/publisher_detail.html'
    context_object_name = 'publisher'

    queryset = Publisher.objects.prefetch_related('book_set__authors')


class StoreList(ListView):
    model = Store
    template_name = 'library/store_list.html'
    context_object_name = 'stores'


class StoreDetail(DetailView):
    model = Store
    template_name = 'library/store_detail.html'
    context_object_name = 'store'
    queryset = Store.objects.prefetch_related('books__authors')

    def get_context_data(self, **kwargs):
        context = super(StoreDetail, self).get_context_data(**kwargs)
        context['book_list'] = Store.objects.filter(pk=self.kwargs.get('pk')).aggregate(
            total_price=Sum('books__price'),
            min_price=Min('books__price'),
            max_price=Max('books__price'),
            avg_price=Avg('books__price'),
            total_pages=Sum('books__pages'),
            average_rating=Avg('books__rating'),
        )
        return context
