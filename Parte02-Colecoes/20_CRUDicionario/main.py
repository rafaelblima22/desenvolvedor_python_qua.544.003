import os

#SECTION - Função para limpar a tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#Criar uma lista de usuarios
usuarios = []

while True:
    #SECTION - Menu de opções
    print(f"{'-'*20} CRUDicionario {'-'*20}")
    print("1 - Cadastrar novo usuario")
    print("2 - Listar todos os usuarios")
    print("3 - Alterar dados de um usuario")
    print("4 - Deletar usuario")
    print("5 - Sair do programa")
    print(f"{'-'*65}")
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
            #TODO - alterar usuario
            pass
        case "4":
            #TODO - Excluir usuario
            pass
        case "5":
            break
        case _:
            print("Opção invalida!")
            continue