import os
from models import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()
    pf = PessoaFisica("rafa","023412","rafa@gmail.com","61981")
    pj = PessoaJuridica("python","123456789","pyhon@cobra.com","8898")

    limpar()

    print(f"Nome: {pf.nome}")
    print(f"CPF: {pf.cpf}")
    print(f"E-mail: {pf.email}")
    print(f"Telefone: {pf.telefone}")

    print(f"{"="*50}")

    print(f"Nome fantasia: {pj.nome_fantasia}")
    print(f"CNPJ: {pj.cnpj}")
    print(f"E-mail: {pj.email}")
    print(f"Telefone: {pj.telefone}")


if __name__ == "__main__":
    main()