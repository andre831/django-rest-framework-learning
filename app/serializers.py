#import models
from app.models import Tenis

#imports rest_framework 
from rest_framework import serializers

class TenisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenis
        fields = ['id', 'nome', 'marca', 'cor', 'preco']
