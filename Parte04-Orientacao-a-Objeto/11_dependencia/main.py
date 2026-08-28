import os
from models import Pedido

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    pedido = Pedido(0.0,0.0)
    limpar()

    pedido.valor1 = float(input("Informe o valor 1: ").replace(",","."))
    pedido.valor2 = float(input("Informe o valor 2: ").replace(",","."))

    limpar()

    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    operador = input("Informe a operação desejada: ").strip()
    print(pedido.calcular_total(operador))

if __name__ == "__main__":
    main()