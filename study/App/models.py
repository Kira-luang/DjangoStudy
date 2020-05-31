from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField(default=23)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=15)

