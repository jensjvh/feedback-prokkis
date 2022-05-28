from rest_framework import serializers
from .models import *

class currentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = currentUser
        fields = ["image", "name", "username"]

class productRequestsSerialzier(serializers.ModelSerializer):
    class Meta:
        model = productRequests
        fields = ["title", "category", "upvotes", "status", "description"]