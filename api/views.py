from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from api import serializers, models
from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaSerializer
    queryset = models.Empresa.objects.all()

class CalculadoraViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CalculadoraSerializer
    queryset = models.Calculadora.objects.all()


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'operando_1': openapi.Schema(type=openapi.TYPE_INTEGER, description='operando'),
        'operando_2': openapi.Schema(type=openapi.TYPE_INTEGER, description='operador'),
        'empresa': openapi.Schema(type=openapi.TYPE_INTEGER, description='id empresa'),
    }
))
@api_view(['POST'])
@csrf_exempt
def soma(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['operador'] = '+'
        data['resposta'] = data['operando_1'] + data['operando_2']
        serializer = serializers.CalculadoraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'operando_1': openapi.Schema(type=openapi.TYPE_INTEGER, description='inteiro'),
        'operando_2': openapi.Schema(type=openapi.TYPE_INTEGER, description='inteiro'),
        'empresa': openapi.Schema(type=openapi.TYPE_INTEGER, description='id empresa'),
    }
))
@api_view(['POST'])
@csrf_exempt
def sub(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['operador'] = '-'
        data['resposta'] = data['operando_1'] - data['operando_2']
        serializer = serializers.CalculadoraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'operando_1': openapi.Schema(type=openapi.TYPE_INTEGER, description='operando'),
        'operando_2': openapi.Schema(type=openapi.TYPE_INTEGER, description='operador'),
        'empresa': openapi.Schema(type=openapi.TYPE_INTEGER, description='id empresa'),
    }
))
@api_view(['POST'])
@csrf_exempt
def multi(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['operador'] = '*'
        data['resposta'] = data['operando_1'] * data['operando_2']
        serializer = serializers.CalculadoraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'operando_1': openapi.Schema(type=openapi.TYPE_INTEGER, description='operando'),
        'operando_2': openapi.Schema(type=openapi.TYPE_INTEGER, description='operador'),
        'empresa': openapi.Schema(type=openapi.TYPE_INTEGER, description='id empresa'),
    }
))
@api_view(['POST'])
@csrf_exempt
def div(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['operador'] = '/'
        data['resposta'] = data['operando_1'] / data['operando_2']
        serializer = serializers.CalculadoraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@swagger_auto_schema(method = 'get', manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY ,
                          type=openapi.TYPE_INTEGER,
                          description='id empresa'),
    ])
@api_view(['GET'])
@cache_page(10 )
@csrf_exempt
def hist(request):
    if request.method == 'GET':
        empresa_id = request.GET.get('id', '')
        empresa_exist = models.Empresa.objects.filter(id=empresa_id).values()
        if empresa_exist:
            historico = models.Calculadora.objects.filter(empresa=empresa_id).values()
            list_contas = {}
            for conta in historico:
                list_contas[conta['id']] = conta
            return JsonResponse(list_contas, status=200)
        
        return JsonResponse({}, status=404)
        
