from rest_framework import serializers

from .models import User, Profile


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


    def create(self, validated_data):
        # Hash the password before saving
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()
        return user
    

class ProfilesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile 
        fields = ["user", "email", "username", "image"]

    def get_email(self, obj):
        return f"{obj.user.email}"

    def get_username(self, obj):
        return f"{obj.user.username}"
    
