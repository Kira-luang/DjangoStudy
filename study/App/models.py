from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=128)
    token = models.CharField(max_length=255)
    class Meta:
        db_table = 'user'

