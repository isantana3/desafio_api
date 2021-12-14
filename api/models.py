from django.db import models


class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.nome_empresa


class Calculadora(models.Model):
    OPERADOR =(
        ("+", "Soma"),
        ("-", "Subtração"),
        ("*", "Multiplicação"),
        ("/", "Divisão"),
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    operando_1 = models.IntegerField()
    operador = models.CharField(max_length=1, choices=OPERADOR, blank=True, null=True)
    operando_2 = models.IntegerField()
    resposta = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.resposta)