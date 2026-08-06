#NOTE - Dicionario de dados
usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulanodetal@gmail.com",
    'cpf': "123.456.789-22"
}

#NOTE - usuario informa a chave que deseja alterar
chave = input("Informe o nome da chave: ").strip().lower()

#TODO - Verificar se a chave existe

#Alterar a chave nome no discionario
usuario['nome'] = input(f"Informe o novo nome de {usuario.get('nome')}:").strip().title()

#NOTE - Imprimir o dicionario
for chave in usuario:
    print(f"{chave.upper()}: {usuario.get(chave)}")