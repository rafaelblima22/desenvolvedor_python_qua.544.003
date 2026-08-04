#imprte de biblioteca
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#lista vazia
limpar()
nomes = []
while True:
    nome = input("Informe o nome: ").strip().title()

    nomes.append(nome)

    print("Deseja inserir mais um nome?")
    print("'s' para sim")
    print("Qualquuer outro valor para não")
    opcao = input("Resposta: ").strip()

    limpar()

    match opcao:
            case 's':
              continue
            case _:
              break

print("Lista de nomes:\n")
for i,nome in enumerate(nomes,start=1):
    print(f"{i}º nome: {nome}")
### 
# for nome in nomes:
#    print (nome)
###