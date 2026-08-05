cidades =[
    "Brasilia",
    "Rio de janeiro",
    "São Paulo",
    "Belo Horizonte",
    "Goiania",
    "Manaus",
    "Fortaleza",
    "Florianopolis"
]

#NOTE - Informar o nome da cidade a ser pesquisada
cidade_pesquisada = input("Informe o nome da cidade a ser pesquisada: ").strip().title()

#NOTE - Retorna o resulatado
print(f"{cidade_pesquisada} encontrada." if cidade_pesquisada in cidades else f"Cidade não encontrada")