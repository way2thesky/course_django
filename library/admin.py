from django.contrib import admin

from library.models import Author, Book, Publisher, Store


class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """

    inlines = [BooksInline]


admin.site.register(Author)
admin.site.register(Store)
admin.site.register(Book)
