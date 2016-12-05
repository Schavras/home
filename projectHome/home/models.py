from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField('release name', default=2000)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return "%s (%s)" % (self.title, self.year)
