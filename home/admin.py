from django.contrib import admin
from .models import FavoriteMovies, Projects

# Register your models here.

admin.site.register(FavoriteMovies)
admin.site.register(Projects)