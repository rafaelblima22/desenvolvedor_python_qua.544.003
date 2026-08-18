# TODO: atividade 05
# Usando recursividade, crie um programa onde o usuário informa um número inteiro e o programa calcula a sequência de Fibonacci até o número informado.
import os

def fibonacci (x, a, b, resultado):
    if resultado == None:
        resultado = []

    if a > x :
        return resultado

    resultado.append(a)
    return(fibonacci(x, b, a+b, resultado))


def main():
    os.system("cls" if os.name=="nt" else "clear")
    x = int(input("Informe um numero para calcular o Fibonacci até ele: ").strip())
    resultado = []
    resultado = fibonacci(x, 0, 1, resultado)

    os.system("cls" if os.name=="nt" else "clear")
    for i in resultado:
        print(i)


if __name__ == "__main__":
    main()