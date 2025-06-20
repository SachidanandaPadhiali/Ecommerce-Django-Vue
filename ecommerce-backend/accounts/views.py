# Import generic views provided by Django REST Framework
from rest_framework import generics

# Import the built-in User model from Django's authentication system
from django.contrib.auth.models import User

# Import your custom serializer to handle User creation
from .serializers import UserSerializer

# Import the AllowAny permission so this view is accessible without authentication
from rest_framework.permissions import AllowAny

# Create a view to handle user registration
class RegisterView(generics.CreateAPIView):
    # Define the queryset—used by DRF internally for validation
    queryset = User.objects.all()

    # Specify which serializer to use for incoming data
    serializer_class = UserSerializer

    # Allow unauthenticated users to access this endpoint (i.e., for sign-up)
    permission_classes = [AllowAny]
