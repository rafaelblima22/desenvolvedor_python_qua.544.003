#TODO - atividade 01
"""
Crie um programa que receba o nome, peso e altura do usuario, e informe na tela o seu IMC o seu diagnostico com base no valor do IMC.
"""
import os
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

nome = input("Informe o seu nome: ").strip()
limpar()

peso = float(input("Informe a sua peso:"))
limpar()

altura = float(input("Informe a sua altura:").replace(",","."))
limpar()

imc = peso/(altura * altura)

print(f"{nome} seu imc é: {imc}")
if(0<imc<=18.5):
    print("Abaixo do peso")
elif(18.5<imc<25):
    print("Peso normal")
elif(25<=imc<30):
    print("Sobrepeso")
elif(30<=imc<35):
    print("Obesidade Grau I")
elif(35<=imc<40):
    print("Obesidade Grau II")
elif(40<=imc):
    print("Obesidade Grau III(Mórbida)")
else:
    print("Erro!")
