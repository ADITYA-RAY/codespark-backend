from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    writer = models.CharField(max_length=120)
    body = models.TextField()

    def _str_(self):
        return self.title
