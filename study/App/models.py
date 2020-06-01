from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=15)
    os_path = models.ImageField(upload_to='%Y%m%d/image')

    class Meta:
        db_table = 'image'
