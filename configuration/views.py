from numpy import product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import currentUser, productRequests
from .serializers import *

class productRequestsList(APIView):

    def get(self, request, format = None):
        productrequests = productRequests.objects.all()
        serializer = productRequestsSerializer(productrequests, many = True)
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

    def delete(self, request):

        productrequest_delete = productRequests.objects.filter(title = request.data.get('title'))
        if not productrequest_delete:
            return Response(
                {"res": "Object with title does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )
        productrequest_delete.delete()
        return Response(
            {"res": "Object deleted!"},
            status = status.HTTP_200_OK
        )
    
    def put(self, request):

        # productrequest_update = productRequests.objects.filter(title = request.data.get('title'))
        productrequest_update = productRequests.objects.get(title = request.data.get('title'))
        if not productrequest_update:
            return Response(
                {"res": "Object with title does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title' : request.data.get('title'),
            'category' : request.data.get('category'),
            'upvotes' : request.data.get('upvotes'),
            'status' : request.data.get('status'),
            'description' : request.data.get('description')
        }
        print(data)
        serializer = productRequestsSerializer(instance = productrequest_update, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):

        productrequest_patch = productRequests.objects.get(title = request.data.get('title'))
        if not productrequest_patch:
            return Response(
                {"res": "Object with title does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title' : request.data.get('title'),
            'category' : request.data.get('category'),
            'upvotes' : request.data.get('upvotes'),
            'status' : request.data.get('status'),
            'description' : request.data.get('description')
        }
        print(data)
        serializer = productRequestsSerializer(instance = productrequest_patch, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)