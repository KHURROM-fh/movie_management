# reporting/serializers.py
from rest_framework import serializers
from .models import MovieReport

class MovieReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReport
        fields = '__all__'  # Adjust to include only necessary fields if needed
