from django.shortcuts import render
from .models import Auto
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import AutoSerializer

# Create your views here.

@api_view (['GET','POST'])
def autos_list (request, format=None):
    
    if request.method == 'GET':
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view (['GET','PUT','DELETE'])
def autos_detail(request,id, format=None):
    
    try:
        auto = Auto.objects.get(pk=id)
    except Auto.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AutoSerializer(auto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AutoSerializer(auto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        auto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
