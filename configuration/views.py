from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import currentUser, productRequests
from .serializers import *

class productRequestsList(APIView):

    def get(self, request, format = None):
        productrequests = productRequests.objects.all()
        serializer = productRequestsSerializer(productrequests)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format = None):
        data = {
            'title' : request.data.get('title'),
            'category' : request.data.get('category'),
            'upvotes' : request.data.get('upvotes'),
            'status' : request.data.get('status'),
            'description' : request.data.get('description')
        }
        serializer = productRequestsSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    

    def delete(self)

    def put()