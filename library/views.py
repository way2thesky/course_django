from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg, Count, Max, Min, Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

from .forms import StoreModelForm
from .models import Author, Book, Publisher, Store

User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'index.html'


class GetRandomBook(TemplateView):
    template_name = 'library/get_random_book.html'

@method_decorator(cache_page(20), name='dispatch')
class AuthorList(ListView):
    model = Author
    paginate_by = 10
    template_name = 'library/author_list.html'
    context_object_name = 'authors'
    queryset = Author.objects.prefetch_related('book_set__authors')


@method_decorator(cache_page(20), name='dispatch')
class AuthorDetail(DetailView):
    model = Author
    template_name = 'library/author_detail.html'
    context_object_name = 'author'


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']
    template_name = 'library/book_create.html'
    success_url = reverse_lazy('library:book-list')


class BookUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Book
    success_message = "Successfully"
    fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']
    template_name = 'library/book_update.html'

    def get_success_url(self):
        book_id = self.kwargs['pk']
        return reverse_lazy('library:book-update', kwargs={'pk': book_id})


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'library/book_delete.html'
    success_url = reverse_lazy('library:book-list')


class BookList(ListView):
    model = Book
    paginate_by = 10
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    queryset = Book.objects.annotate(num_authors=Count('authors')).select_related('publisher') \
        .prefetch_related('authors__book_set')


@method_decorator(cache_page(20), name='dispatch')
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


@method_decorator(cache_page(20), name='dispatch')
class PublisherList(ListView):
    model = Publisher
    paginate_by = 10
    template_name = 'library/publisher_list.html'
    context_object_name = 'publishers'


@method_decorator(cache_page(20), name='dispatch')
class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'library/publisher_detail.html'
    context_object_name = 'publisher'

    queryset = Publisher.objects.prefetch_related('book_set__authors')


@method_decorator(cache_page(20), name='dispatch')
class StoreList(ListView):
    model = Store
    paginate_by = 10
    queryset = Store.objects.prefetch_related('books')
    template_name = 'library/store_list.html'
    context_object_name = 'stores'


@method_decorator(cache_page(20), name='dispatch')
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


def store_create(request):
    if request.method == 'POST':
        form = StoreModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            text = f'You added {name}.'

    else:
        form = StoreModelForm()
    context = {'form': form,}
    return render(request, 'store_create.html', {'context': context})
