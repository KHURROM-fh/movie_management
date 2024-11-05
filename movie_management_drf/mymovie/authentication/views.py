from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
