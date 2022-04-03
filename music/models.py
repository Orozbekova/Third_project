from django.db import models

# Create your models here.

class Category(models.Model):
    slug = models.SlugField(max_length=30,primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ForeignKey(Category,related_name='genre',on_delete=models.CASCADE)
    singer = models.CharField(max_length=50)
    file = models.FileField(upload_to='',storage=None,max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return self.name