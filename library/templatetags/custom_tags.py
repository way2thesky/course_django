import re

from django import template
from django.utils.safestring import mark_safe

from library.models import Book

register = template.Library()


@register.simple_tag
def get_random_book():
    some_book = Book.objects.filter(rating__lte=4.5).order_by('?').first()

    if some_book:
        name = some_book.name
        authors_list = [author.name for author in some_book.authors.all()]
        separator = ", "
        authors = separator.join(authors_list)
        result = f"Book: {name} <br> Authors: {authors}"
        return mark_safe(result)


@register.inclusion_tag('store_form.html')
def store_form(form):
    return form


@register.filter
def modify_string(value):
    word_list = [
        "Neque", "porro", "quisquam", "est", "qui", "dolorem",
        "ipsum", "quia", "dolor", "sit", "sit", "consectetur",
        "adipisci", "velit", "amet", "Нет", "никого", "кто", "любил", "бы", "боль",
        "саму", "по", "себе", "кто", "искал", "бы",
        "её", "и", "кто", "хотел", "бы", "иметь", "её", "просто", "потому", "что", "это", "боль"
    ]
    for word in word_list:
        rep = "*" * len(word)
        value = re.sub(r'\b' + re.escape(word) + r'\b', rep, value)

    return value


@register.filter
def currency(value, name='UAH'):
    return f'{value}, {name}'
