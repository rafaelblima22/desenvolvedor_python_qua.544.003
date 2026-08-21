import os

from models import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="", endereco="")
    empresa = PessoaJuridica("","","","","","")

    #SECTION - informar os valores de usuario
    usuario.nome = input("Informe o nome do usuario: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o E-mail: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereco: ")

    limpar()

    #SECTION - Informa dados da empresa
    empresa.razao_social = input("Informe o nome juridico da empresa: ").strip()
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.email = input("Informe o E-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereco da empresa: ")

    limpar()

    usuario.exibir_dados()
    print(f"{"="*50}")
    empresa.exibir_dados()

if __name__ == "__main__":
    main()