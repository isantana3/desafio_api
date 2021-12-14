from django.contrib import admin

from .models import Calculadora, Empresa

@admin.register(Calculadora)
class CalculadoraAdmin(admin.ModelAdmin):
    list_display = ('operando_1', 'operador', 'operando_2', 'resposta')

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_empresa', 'cnpj')