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
        User.objects.filter(~Q(is_superuser=True) | ~Q(is_staff=True)).delete()
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        authors = [Author(name=fake.name(), age=random.randint(20, 70)) for _ in range(1, 6)]
        Author.objects.bulk_create(authors)
        # create 5 publishers
        publishers = [Publisher(name=fake.company()) for _ in range(1, 6)]
        Publisher.objects.bulk_create(publishers)
        # create 20 books for every publishers
        books = []
        counter = 0
        for publisher in Publisher.objects.all():
            for i in range(20):
                counter = counter + 1
                books.append(
                    Book(
                        name=fake.sentence(),
                        price=random.uniform(29.99, 225.9),
                        pages=random.randint(50, 300),
                        rating=round(random.uniform(1, 5), 2),
                        pubdate=timezone.now(),
                        publisher=publisher)
                )
        Book.objects.bulk_create(books)

        # create 10 stores and insert 10 books in every store
        books = list(Book.objects.all())
        for i in range(10):
            temp_books = [books.pop(0) for i in range(10)]
            store = Store.objects.create(name=f"Store{i + 1}")
            store.books.set(temp_books)
            store.save()
        self.stdout.write(self.style.SUCCESS('ADD CONNECTIONS'))
