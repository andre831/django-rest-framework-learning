from django.shortcuts import render

#import class in serializer
from app.serializers import TenisSerializer

#imports models
from app.models import Tenis

#imports rest_framework
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status

#methods for acess in view
@api_view(['GET', 'POST'])
def tenis_list(request):

    #return all products
    while(request.method == 'GET'): 
        tenis = Tenis.objects.all()
        serializer = TenisSerializer(tenis, many = True)
        return Response(serializer.data)

    #for post, return the data and save
    if request.method == 'POST':
        serializer = TenisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        #for error, response 'status'
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#get details, changes and delete object
@api_view(['GET', 'PUT', 'DELETE'])
def tenis_sett(request, pk):

    #get object in database
    try:
        tenis = Tenis.objects.get(pk=pk)
    
    #in case don't found object, return:
    except Tenis.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #get object
    if request.method == 'GET':
        serializer = TenisSerializer(tenis)
        return Response(serializer.data)

    # for changes, happen request > valid data > save
    elif request.method == 'PUT':
        serializer = TenisSerializer(tenis, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        #in error case, response 404
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # for delete, return message successfully 
    elif request.method == 'DELETE':
        tenis.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)