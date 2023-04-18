from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=255)


class Movie(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    year = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    video = models.FileField()


