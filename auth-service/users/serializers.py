    
from rest_framework import serializers
from .models import User
import uuid

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        base = f"{validated_data['first_name'].lower()}.{validated_data['last_name'].lower()}"
        # remove spaces in case of compound names
        base = base.replace(' ', '')
        username = base
        while User.objects.filter(username=username).exists():
            username = f"{base}.{uuid.uuid4().hex[:4]}"

        user = User.objects.create_user(
            username=username,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            role='CLIENT'
        )
        return user