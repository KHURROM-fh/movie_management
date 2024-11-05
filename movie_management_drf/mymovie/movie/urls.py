# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, RatingViewSet, MovieReportViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')  
router.register(r'ratings', RatingViewSet, basename='ratings')  
router.register(r'reports', MovieReportViewSet, basename='reports')  

urlpatterns = [
    path('', include(router.urls)),
]
