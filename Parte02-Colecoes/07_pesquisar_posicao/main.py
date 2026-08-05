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
cidade = input("Informe o nome da cidade a ser pesquisada: ").strip().title()

if cidade in cidades :
    indice = cidades.index(cidade)
    print(f"Indice de  {cidade} na lista é {indice}.")
else:
        print("Cidade não encontrada")