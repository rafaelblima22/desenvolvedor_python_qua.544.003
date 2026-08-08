import os

#SECTION - Função para limpar a tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#Criar uma lista de usuarios
usuarios = [
    {
        'nome': "Fulano",
        'cpf': "22222",
        'email': "fulano@gmail.com"
    },
    {
            'nome': "Cicrano",
            'cpf': "22222",
            'email': "cicrano@gmail.com"
    },
    {
        'nome': "Beltrano",
        'cpf': "2222222",
        'email': "beltrano@gmail.com"
    },
]

while True:
    #SECTION - Menu de opções
    print(f"{'-'*20} CRUDicionario {'-'*20}")
    print("1 - Cadastrar novo usuario")
    print("2 - Listar todos os usuarios")
    print("3 - Alterar dados de um usuario")
    print("4 - Deletar usuario")
    print("5 - Sair do programa")
    print(f"{'-'*60}")
    opcao = input("Informe a opção desejada: ").strip()
    limpar()

    match opcao:
        case "1":
            #SECTION - Criar novo usuario
            usuario = {}
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['cpf'] = input("Informe o cpf: ").strip()
            usuario['email'] = input("Informe o email: ").strip().lower()

            #NOTE - adicionar usuario na lista
            usuarios.append(usuario)
            limpar()
            continue
        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*65}")
            continue
        case "3":
            #SECTION - alterar usuario
            nome = input("Informe o nome a ser pesquisado: ").strip().title()
            for usuario in usuarios:
                if nome in usuario['nome']:
                    #2º menu
                    print(f"{'-'*65}")
                    print("nome")
                    print("cpf")
                    print("email")
                    print("Cancelar")
                    print(f"{'-'*65}")
                    alterar = input("O que deseja alterar ").strip().lower()
                    if alterar in usuario:
                        limpar()
                        usuario[alterar] = input("Voce deseja alterar para: ").strip()
                        limpar()
                        print("Alterado com sucesso!")
                    else:
                        print("Usuario não encontrado. ")


        case "4":
            #REVIEW - Excluir usuario
            nome = input("Informe o nome a ser deletado: ").strip().title()
            for usuario in  usuarios:
                if nome in usuario['nome']:
                    usuarios.remove(usuario)
                    print("Usuario deletado com sucesso")
                else:
                    print("Usuario não encontrado.")
            continue
        case "5":
            break
        case _:
            print("Opção invalida!")
            continue