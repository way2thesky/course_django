from django import template
from django.core.cache import cache
from django.utils.safestring import mark_safe

from library.models import Book

import requests

register = template.Library()


@register.simple_tag
def get_random_book():
    some_book = Book.objects.order_by('?').first()
    if some_book:
        name = some_book.name
        authors_list = [author.name for author in some_book.authors.all()]
        separator = ", "
        authors = separator.join(authors_list)
        result = f"Random value from DB: <br> Book: {name} <br> Authors: {authors}"
        return mark_safe(result)


@register.filter
def check_forbidden_words(word):
    forbidden_words = cache.get('forbidden_words')
    if forbidden_words is None:
        forbidden_words = requests.get('https://random-word-api.herokuapp.com/word?number=100').text
        cache.set('forbidden_words', forbidden_words, 30)

    if word in forbidden_words:
        word.replace(word, '***' * len(word))
    return word


@register.inclusion_tag('store_form.html')
def store_form(form):
    return form
