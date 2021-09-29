from django.shortcuts import render
from rest_framework.exceptions import NotFound

#import class in serializer
from app.serializers import TenisSerializer

#imports models
from app.models import Tenis

#imports rest_framework
from rest_framework.views import  APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status

class Tenis_List(APIView):

    #return all products
    def get(self, request):
        tenis = Tenis.objects.all()
        serializer = TenisSerializer(tenis, many = True)
        return Response(serializer.data)
        
    #for post, return the data and save
    def post(self, request):
        serializer = TenisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        #for error, response 'status'
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#methods for acess in view
class Tenis_Details(APIView):

    def get_object(self, pk):
        #get object in database
        try:
            return Tenis.objects.get(pk=pk)
        
        #in case don't found object, return:
        except Tenis.DoesNotExist:
            raise NotFound()

    #get object
    def get(self, request, pk):
        tenis = self.get_object(pk)
        serializer = TenisSerializer(tenis)
        return Response(serializer.data)

    # for changes, happen request > valid data > save
    def put(self, request, pk):
        tenis = self.get_object(pk)
        serializer = TenisSerializer(tenis, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        #in error case, response 404
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # for delete, return message successfully 
    def delete(self, request, pk):
        tenis = self.get_object(pk)
        tenis.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


 
