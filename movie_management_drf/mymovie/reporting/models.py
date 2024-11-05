from django.db import models
from movie.models import Movie
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieReport(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Report for {self.movie.title} by {self.reported_by.username}"
