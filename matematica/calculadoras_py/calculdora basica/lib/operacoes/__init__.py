# todo processamento será realizado neste arquivo para manter a organização no código

import math 

def somar(a, b):
    return float(a) + float(b)

def multiplicar(a, b):
    return float(a) * float(b)

def subtrair(a, b):
    return float(a) - float(b)

def divisao(a, b):
    if float(b) == 0:
        return "Erro: Divisão por zero!"
    return float(a) / float(b)

def raiz_quadrada(a):
    return math.sqrt(float(a))

def quadrado(a):
    return float(a) ** 2