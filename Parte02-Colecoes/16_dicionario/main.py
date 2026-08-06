#NOTE - Dicionario de dados
usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulanodetal@gmail.com",
    'cpf': "123.456.789-22"
}

#NOTE - Exibindo os dados do dicionario
#Forma 1
print("Forma1")
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"Email: {usuario['email']}")
print(f"CPF: {usuario['cpf']}")

#Forma 2
print("\nForma2")
print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"Email: {usuario.get('email')}")
print(f"CPF: {usuario.get('cpf')}")

#Forma 3
print("\nForma3")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")