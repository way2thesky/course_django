import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from faker import Faker

from library.models import Author, Book, Publisher, Store

fake = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arg', type=int)

    def handle(self, *args, **options):
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        num = options['arg']
        # create  authors
        authors = [Author(name=fake.name(), age=random.randint(20, 70)) for _ in range(int(num))]
        Author.objects.bulk_create(authors)

        # create  publishers
        publishers = [Publisher(name=fake.company()) for _ in range(int(num))]
        Publisher.objects.bulk_create(publishers)

        # create books for every publishers
        for publisher in Publisher.objects.all():
            books = [Book(
                name=fake.sentence(),
                price=random.uniform(29.99, 225.9),
                pages=random.randint(50, 300),
                rating=round(random.uniform(1, 5), 2),
                pubdate=timezone.now(),
                publisher=publisher, )
                for _ in range(20)]
            Book.objects.bulk_create(books)
        # create  stores and insert books in every store
        for _ in range(int(num)):
            books = Book.objects.all()
            store = Store.objects.create(name=fake.company())
            authors_books_ids = books[:random.randint(1, len(books))]
            random.shuffle(authors_books_ids)
            store.books.set(authors_books_ids)

        books_id = list(Book.objects.values_list('id', flat=True))
        authors_id = Author.objects.values_list('id', flat=True)

        for author_id in authors_id:
            books = []
            random.shuffle(books_id)
            authors_books_ids = books_id[:random.randint(1, len(books_id))]

            for book_id in authors_books_ids:
                # through is the table generated by django to link m2m between Book and Author
                book = Book.authors.through(book_id=book_id, author_id=author_id)
                books.append(book)

            Book.authors.through.objects.bulk_create(books, batch_size=7000)
