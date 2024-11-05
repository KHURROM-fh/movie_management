from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('reports', views.MovieReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
