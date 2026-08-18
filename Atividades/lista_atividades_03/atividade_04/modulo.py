import math
import os

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def potencia(x,y):
    return math.pow(x,y)

def raiz_quadrada(x):
    return math.isqrt(x)

def calcular_paralelepipidico(comprimento, largura, altura):
    return comprimento*largura*altura

def calcular_cilindro(raio, altura):
    return math.pi * (raio ** 2) * altura
