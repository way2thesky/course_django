import random
from django.utils import timezone
from annotate_aggregate.models import Author, Book, Store, Publisher
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arg', type=int)

    def handle(self, *args, **options):
        num = options['arg']

        for _ in range(int(num)):
            Author.objects.create(name=fake.name(), age=random.randint(20, 70))

        for _ in range(int(num)):
            Publisher.objects.create(name=fake.company())

            for publisher in Publisher.objects.all():
                for _ in range(int(num)):
                    books = [Book(
                        name=fake.sentence(),
                        price=random.uniform(29.99, 225.9),
                        pages=random.randint(50, 300),
                        rating=round(random.uniform(1, 5), 2),
                        pubdate=timezone.now(),
                        publisher=publisher)]
                    Book.objects.bulk_create(books)

        objs = Book.objects.all()
        for _ in range(int(num)):
            store = Store.objects.create(name=fake.company())
            store.books.set(objs)
            store.save()
