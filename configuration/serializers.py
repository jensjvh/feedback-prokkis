from rest_framework import serializers
from .models import *

class currentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = currentUser
        fields = ["image", "name", "username"]

class productRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = productRequests
        fields = ["title", "category", "upvotes", "status", "description", "comment"]

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "productrequest"]