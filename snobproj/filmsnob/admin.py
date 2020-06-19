from django.contrib import admin
from .models import Movies, Review

# Register your models here.
admin.site.register(Movies)
admin.site.register(Review)