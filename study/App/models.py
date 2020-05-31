from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'animal'


class Cat(Animal):
    eat = models.CharField(max_length=15)

    class Meta:
        db_table = 'cat'


class Dog(Animal):
    legs = models.IntegerField()

    class Meta:
        db_table = 'dog'
