from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to= "images/projects/")
    srclink = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class FavoriteMovies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to= "images/")
    rating = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} - {self.rating}"

