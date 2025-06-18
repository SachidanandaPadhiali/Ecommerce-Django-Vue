from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # Write-only field to accept a password during registration.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        # Use Django’s built-in create_user function to handle password hashing.
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user