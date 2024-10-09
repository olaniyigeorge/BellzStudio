from .models import Note, IdeaTag
from rest_framework import serializers



class IdeaTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = IdeaTag
        fields = "__all__" 

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = "__all__" 
