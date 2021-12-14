from django.db.models import fields
from rest_framework import serializers
from api import models

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'

class CalculadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Calculadora
        fields = '__all__'


