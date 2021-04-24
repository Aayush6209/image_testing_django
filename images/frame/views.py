from django.shortcuts import render
from .models import IMAGES
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def upload_view(request):
    if request.method == 'POST':
        serializer = universal_serializer(data=request.data)
        if serializer.is_valid():
            image = IMAGES.objects.create(
                photo=serializer.data['photo']
            )
            image.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_view(request, pk):
    if request.method == 'PUT':
        image = IMAGES.objects.get(pk=pk)
        serializer = universal_serializer(data=request.data)
        if serializer.is_valid():
            image.photo = serializer.data['photo']
            image.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_view(request, pk):
    if request.method == 'DELETE':
        image = IMAGES.objects.get(pk=pk)
        image.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def download_view(request, pk):
    if request.method == 'GET':
        image = IMAGES.objects.get(pk=pk)

        return Response(
            {"path": f"{'uploads'}/{image.name}"},
            status=status.HTTP_200_OK
        )
    return Response(status=status.HTTP_400_BAD_REQUEST)
