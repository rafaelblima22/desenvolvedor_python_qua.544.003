import os
from models import PessoaFisica,PessoaJuridica

def limpar():
    os.system("cls" if os.name =="nt" else "clear")

def main():
    usuario = PessoaFisica("","","","","",0,0.0)
    empresa = PessoaJuridica("","","","","",0.0)

    limpar()

    usuario.nome = "rafa"
    usuario.cpf = "023412"
    usuario.profissao = "TI"
    usuario.idade = 32
    usuario.telefone = "9818898"
    usuario.email = "rafa@gmail.com"
    usuario.salario = 54321.55

    empresa.nome_fantasia = "Jabiraca"
    empresa.razao_social = "Não sei"
    empresa.cnpj = "1230"
    empresa.telefone = "7201594"
    empresa.email = "jabiraca@gmail.com"
    empresa.valor_mercado = 78974.33

    limpar()

    print(usuario)
    print(empresa)

    del(usuario)
    del(empresa)


if __name__ == "__main__":
    main()