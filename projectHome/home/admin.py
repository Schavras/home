from django.contrib import admin

# Register your models here.
from .models import Movie, Category

admin.site.register(Movie)
admin.site.register(Category)
