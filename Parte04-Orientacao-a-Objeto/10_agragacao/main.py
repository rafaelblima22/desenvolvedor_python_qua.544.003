import os
from models import Empresa,Departamento

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    departamento = Departamento("")
    empresa = Empresa("",departamento)

    limpar()

    empresa.nome = input("Informe o nome da empresa: ")
    empresa.departamento.nome = input("Informe o nome do departamento: ")

    limpar()

    print(empresa.detalhes())

if __name__ == "__main__":
    main()