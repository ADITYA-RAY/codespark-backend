from django.db import models

# Create your models here.


class Trending(models.Model):
    date = models.DateField( auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    description = models.TextField(max_length=80)
    link=models.CharField(max_length=200)
    imgsrc= models.CharField(max_length=200)

    def _str_(self):
        return self.title
