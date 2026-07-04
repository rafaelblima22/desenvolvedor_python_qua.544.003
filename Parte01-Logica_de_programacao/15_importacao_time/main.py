#SECTION - importação
import os
import time

#NOTE - Tratamento de excessao
try:
    #SECTION - Entrada de dados
    n = int(input("Informe um numero inteiro: "))

    #NOTE - Limpa tela
    os.system("cls" if os.name == "nt" else "clear")

    #NOTE - contagem
    while n >= 0:
        print(f"{n}...")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        n -= 1

    print("💣BOOOOOOOMMMMMM!!!!!💣")
except Exception as e:
    print(f"Não foi possivel iniciar a contagem. {e}.")