from django.db import models


# Create your models here.

class MyPortfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="D:\\pycharm\\portfolio\\static")
