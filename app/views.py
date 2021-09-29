from django.shortcuts import render

#import class in serializer
from app.serializers import TenisSerializer

#imports models
from app.models import Tenis

#imports rest_framework
from rest_framework.decorators import  api_view
from rest_framework.response import Response

#methods for acess in view
@api_view(['GET'])
def tenis_list(request):
    tenis = Tenis.objects.all()
    serializer = TenisSerializer(tenis, many = True)
    return Response(serializer.data)

