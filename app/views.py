from django.shortcuts import render

#import class in serializer
from app.serializers import TenisSerializer

#imports models
from app.models import Tenis

#imports rest_framework
from rest_framework.decorators import  api_view
from rest_framework.response import Response

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
       
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

