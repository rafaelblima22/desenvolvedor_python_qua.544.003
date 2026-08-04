#TODO - atividade 02
"""
Crie um programa que receba uma vez o nome e a idade do usuario, e em seguida mostre os filmes em cartaz em 5 salas de cinema:
- A volta dos que não foram (livre)
- A roda quadrada (12 anos)
- As tranças do rei careca (14 anos)
- Poeira em alto mar (16 anos)
- A viganca do frango assado (18 anos)
O usuario irá escolher a sala onde o filme desejado esta passando. Caso o usuario não tenha idade, o programa impede sua entrada e re-exibe a lista para que o mesmo possa escolher outro filme. Caso o usuario tenha idade minima, o programa grava em arquivo o bilhete do filme e encerra o programa.
"""
import os
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

nome = input("Informe o seu nome: ").strip()
limpar()

idade = int(input("Informe a sua idade:"))
limpar()
while(True):

    print("Lista de filmes: ")
    print("1 - A volta dos que não foram (livre)")
    print("2 - A roda quadrada (12 anos)")
    print("3 - As tranças do rei careca (14 anos)")
    print("4 - Poeira em alto mar (16 anos)")
    print("5 - A viganca do frango assado (18 anos)")

    opcao = input("Escolha o filme desejado: ")
    limpar()
    match opcao:
        case"1":
            with open(f"programa_02-01/bilhete/filme1.txt","w", encoding="utf-8")as f:
                f.write(f"Nome:{nome} Idade:{idade}")
            break
        case"2":
            if(idade>=12):
                with open(f"programa_02-01/bilhete/filme2.txt","w", encoding="utf-8")as f:
                    f.write(f"Nome:{nome} Idade:{idade}")
                break
            else:
                print("Não possui a idade minima")
                continue
        case"3":
            if(idade>=14):
                with open(f"programa_02-01/bilhete/filme3.txt","w", encoding="utf-8")as f:
                    f.write(f"Nome:{nome} Idade:{idade}")
                break
            else:
                print("Não possui a idade minima")
                continue
        case"4":
            if(idade>=16):
                with open(f"programa_02-01/bilhete/filme4.txt", "w", encoding="utf-8")as f:
                    f.write(f"Nome:{nome} Idade:{idade}")
                break
            else:
                print("Não possui a idade minima")
                continue
        case"5":
            if(idade>=18):
                with open(f"programa_02-01/bilhete/filme5.txt","w", encoding="utf-8")as f:
                   f.write(f"Nome:{nome} Idade:{idade}")
                break
            else:
                print("Não possui a idade minima")
                continue
        case _:
            print("opção invalida!")
            continue