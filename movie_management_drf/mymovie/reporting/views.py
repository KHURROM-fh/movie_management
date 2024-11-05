# reporting/views.py
from rest_framework import viewsets, permissions
from .models import MovieReport
from .serializer import MovieReportSerializer

class MovieReportViewSet(viewsets.ModelViewSet):
    queryset = MovieReport.objects.all()
    serializer_class = MovieReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)
