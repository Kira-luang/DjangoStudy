from django.db import models

# Create your models here.
class Man(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField(default=25)


class Women(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField(default=23)
    husband = models.OneToOneField('Man', on_delete=models.PROTECT, null=True)

    def meet(self, man):
        self.husband = man
        return self
