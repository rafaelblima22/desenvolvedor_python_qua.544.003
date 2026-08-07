#NOTE - Dicionario de dados
usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulanodetal@gmail.com",
    'cpf': "123.456.789-22"
}

#NOTE - usuario informa a chave que deseja alterar
chave = input("Informe o nome da chave: ").strip().lower()

if chave in usuario:
    #usuario informa o novo valor para a chave
    usuario[chave] = input(f"Informe o novo valor para {chave}: ").strip()

    #NOTE - Imprimir o dicionario
    for chave, valor in usuario.items():
        print(f"{chave.upper()}: {valor}")
else:
    print("Chave nao encontrada.")
