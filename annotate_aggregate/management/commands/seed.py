import random
from django.utils import timezone
from annotate_aggregate.models import Author, Book, Store, Publisher
from django.db.models import Q
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()


class Command(BaseCommand):

    def handle(self, *args, **options):
        authors = [Author(name=fake.name(), age=random.randint(20, 70)) for _ in range(1, 6)]
        Author.objects.bulk_create(authors)

        # create 5 publishers

        publishers = [Publisher(name=fake.company()) for _ in range(1, 6)]
        Publisher.objects.bulk_create(publishers)
        # create 20 books for every publishers

        for publisher in Publisher.objects.all():
            for i in range(1, 6):
                books = [Book(
                    name=fake.sentence(),
                    price=random.uniform(29.99, 225.9),
                    pages=random.randint(50, 300),
                    rating=round(random.uniform(1, 5), 2),
                    pubdate=timezone.now(),
                    publisher=publisher)]
                Book.objects.bulk_create(books)
        # create 10 stores and insert 10 books in every store
        books = list(Book.objects.all())
        for i in range(10):
            temp_books = [books.pop(0) for _ in range(10)]
            store = Store.objects.create(name=fake.company())
            store.books.set(temp_books)
            store.save()
        self.stdout.write(self.style.SUCCESS('OK'))