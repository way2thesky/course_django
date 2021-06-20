from django.contrib import admin
from annotate_aggregate.models import Author, Publisher, Store, Book

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)

