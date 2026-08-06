#NOTE - Dicionario de dados
usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulanodetal@gmail.com",
    'cpf': "123.456.789-22"
}

#Adicionar a chave telefone ao discionario
usuario['telefone'] = input(f"Informe o telefone de {usuario.get('nome')}:").strip()

for chave in usuario:
    print(f"{chave.upper()}: {usuario.get(chave)}")