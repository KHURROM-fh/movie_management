from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Add any viewsets for other models here if necessary, for example: router.register('profile', views.UserProfileViewSet)
router.register('registation', views.UserRegistrationView)
router.register('login', views.UserLoginView)
router.register('profile', views.UserProfileView)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
