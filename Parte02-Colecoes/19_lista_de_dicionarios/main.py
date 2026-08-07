usuarios = [
    {
        'nome': "Fulano",
        'idade': 18,
        'email': "fulano@gmail.com"
    },
    {
            'nome': "Cicrano",
            'idade': 22,
            'email': "cicrano@gmail.com"
    },
    {
        'nome': "Beltrano",
        'idade': 38,
        'email': "beltrano@gmail.com"
    },
]

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")