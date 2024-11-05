# views.py
from rest_framework import viewsets, permissions
from .models import Movie, Rating, MovieReport
from .serializers import MovieSerializer, RatingSerializer, MovieReportSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()  # Ensure queryset is defined
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()  # Ensure queryset is defined
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MovieReportViewSet(viewsets.ModelViewSet):
    queryset = MovieReport.objects.all()  # Ensure queryset is defined
    serializer_class = MovieReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)
