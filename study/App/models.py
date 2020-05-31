from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=15)


class Goods(models.Model):
    name = models.CharField(max_length=15)
    customer_id = models.ManyToManyField('Customer')


'''自管理模板参考'''


class Software(models.Model):
    name = models.CharField(max_length=15)


class User(models.Model):
    name = models.CharField(max_length=15)


class Relation(models.Model):
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    softwareid = models.ForeignKey('Software', on_delete=models.CASCADE)

    class Meta:
        db_table = 'relation'
        unique_together = ('userid', 'softwareid')
