from django.db import models

class Tenis(models.Model):
    nome  = models.CharField(max_length = 80)
    marca = models.CharField(max_length = 50)
    cor   = models.CharField(max_length = 20)
    preco = models.DecimalField(max_digits = 5, decimal_places = 2)
    