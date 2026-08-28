import os
from models import Pessoa

def limpar():
    os.system("cls" if os.name =="nt" else "clear")

def main():
    limpar()

    pessoa1 = Pessoa("",0,0.0)

    pessoa1.nome = input("Digite o nome da pessoa: ").strip().title()
    pessoa1.idade = int(input("Digite a idade da pessoa: "))
    pessoa1.altura = float(input("Digite a altura da pessoa: ").replace(",","."))

    limpar()

    print(f"Nome: {pessoa1.nome}")
    print(f"Idade: {pessoa1.idade}")
    print(f"Altura: {pessoa1.altura}")

if __name__ == "__main__":
    main()