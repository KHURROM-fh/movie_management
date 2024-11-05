from django.db import models
from django.db.models import Avg, Count
from django.contrib.auth import get_user_model

User = get_user_model()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    released_at = models.DateField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')
    avg_rating = models.FloatField(default=0.0)
    total_rating = models.IntegerField(default=0)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def update_total_rating(self):
        ratings = Rating.objects.filter(movie=self)
        self.total_rating = ratings.count()
        self.avg_rating = ratings.aggregate(average=Avg('rating'))['average'] or 0
        self.save(update_fields=['avg_rating', 'total_rating'])


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.movie.update_total_rating()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.movie.update_total_rating()
