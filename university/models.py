from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)
    built = models.DateField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
