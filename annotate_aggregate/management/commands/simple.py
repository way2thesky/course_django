# import random
# from django.utils import timezone
# from annotate_aggregate.models import Author, Book, Store, Publisher
# from django.db.models import Q
# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
# from faker import Faker
#
# fake = Faker()
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         User.objects.filter(~Q(is_superuser=True) | ~Q(is_staff=True)).delete()
#         Publisher.objects.all().delete()
#         Book.objects.all().delete()
#         Store.objects.all().delete()
#
#         authors = [Author(name=fake.name(), age=random.randint(20, 70)) for _ in range(1, 10)]
#         Author.objects.bulk_create(authors)
#
#         publishers = [Publisher(name=fake.company()) for _ in range(1, 11)]
#         Publisher.objects.bulk_create(publishers)
#         books = []
#         counter = 0
#         for publisher in Publisher.objects.all():
#             for i in range(10):
#                 counter = counter + 1
#                 books.append(
#                     Book(name=f"Book{counter}",
#                          price=random.uniform(29.99, 225.9),
#                          pages=random.randint(50, 300),
#                          rating=round(random.uniform(1, 5), 2),
#                          pubdate=timezone.now(),
#                          publisher=publisher))
#         Book.objects.bulk_create(books)
#
#         # create 10 stores and insert 10 books in each store
#         books = list(Book.objects.all())
#         for i in range(10):
#             temp_books = [books.pop(0) for i in range(10)]
#             store = Store.objects.create(name=f"Store{i + 1}")
#             store.books.set(temp_books)
#             store.save()
#         self.stdout.write(self.style.SUCCESS('ADD CONNECTIONS'))




import random
from django.utils import timezone
from annotate_aggregate.models import Author, Book, Store, Publisher
from django.db.models import Q
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()


# def generate_book(number: int) -> dict:
#
#     dict_user = {
#         'first_name': '',
#         'last_name': '',
#         'city': '',
#         'product': []
#     }
#     fake = Faker(['en_US'])
#     first_name = fake.first_name()
#     last_name = fake.last_name()
#     city_id = random.randint(1, number)
#
#     dict_user['first_name'] = first_name
#     dict_user['last_name'] = last_name
#     dict_user['city'] = city_id
#     for _ in range(random.randint(1, 3)):
#         dict_user['product'].append(random.randint(1, number))
#
#     return dict_user
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         User.objects.filter(~Q(is_superuser=True) | ~Q(is_staff=True)).delete()
#         Publisher.objects.all().delete()
#         Book.objects.all().delete()
#         Store.objects.all().delete()
#
#         authors = [Author(name=fake.name(), age=random.randint(20, 70)) for _ in range(1, 10)]
#         Author.objects.bulk_create(authors)
#
#         publishers = [Publisher(name=fake.company()) for _ in range(1, 11)]
#         Publisher.objects.bulk_create(publishers)
#
#         books = []
#         counter = 0
#         for publisher in Publisher.objects.all():
#             for i in range(10):
#                 counter = counter + 1
#                 books.append(
#                     Book(name=f"Book{counter}",
#                          price=random.uniform(29.99, 225.9),
#                          pages=random.randint(50, 300),
#                          rating=round(random.uniform(1, 5), 2),
#                          pubdate=timezone.now(),
#                          publisher=publisher))
#         Book.objects.bulk_create(books)
#
#         # create 10 stores and insert 10 books in each store
#         books = list(Book.objects.all())
#         for i in range(10):
#             temp_books = [books.pop(0) for i in range(10)]
#             store = Store.objects.create(name=f"Store{i + 1}")
#             store.books.set(temp_books)
#             store.save()
#         self.stdout.write(self.style.SUCCESS('ADD CONNECTIONS'))
