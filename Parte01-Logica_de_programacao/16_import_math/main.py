#SECTION - Importação de biblioteca
import math

#NOTE - tratamento de excessao

try:
    while True:
        #NOTE - VAlor do raio
        r = float(input("Informe o valor do raio: ").replace(",","."))

        #NOTE - calcular area do circulo

        area = math.pi * r**2
        print(f"A area do circulo é: {area:.2f}.")

            #NOTE - Menu
        print("1 - Calcular outro circulo")
        print("2 - Sair do programa")
    
        opcao = input("Informe a opção desejada: ").strip()
    
        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("Opção invalida!")
                continue

except Exception as e:
    print(f"Não foi possivel calcular. {e}.")