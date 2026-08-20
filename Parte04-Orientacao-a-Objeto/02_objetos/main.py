import os

from models import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    homem = Pessoa(nome="", idade=0, email="", telefone="")
    mulher = Pessoa(nome="", idade=0, email="", telefone="")

    limpar()

    #SECTION - Informar dados do homem
    homem.nome = input("Indorme o nome do homem: ").strip().title()
    homem.idade = int(input("Informe a idade do homem: "))
    homem.email = input("Informe o e-mail do homem: ")
    homem.telefone = input("Informe o telefone do homem: ").strip()

    limpar()
    
    #SECTION - Informar dados do mulher
    mulher.nome = input("Indorme o nome do mulher: ").strip().title()
    mulher.idade = int(input("Informe a idade do mulher: "))
    mulher.email = input("Informe o e-mail do mulher: ")
    mulher.telefone = input("Informe o telefone do mulher: ").strip()
    limpar()

    print(homem.apresentar())
    print(mulher.cumprimentar(homem.nome))
    print(homem.cumprimentar(mulher.nome))


if __name__ == "__main__":
    main()