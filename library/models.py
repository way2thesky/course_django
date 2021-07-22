from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300, unique=True)
    books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
