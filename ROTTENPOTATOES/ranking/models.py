from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    image = models.CharField(max_length=4)
    rate = models.FloatField(max_length=4)
    description = models.CharField(max_length=300)
    director = models.CharField(max_length=50, default=" ")

    movies_manager = models.Manager()

    def __str__(self):
        return f"{self.name} ({self.release_year})"
