# serializers.py
from rest_framework import serializers
from .models import Movie, Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'  # or specify the exact fields you want

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['movie', 'user', 'rating']
