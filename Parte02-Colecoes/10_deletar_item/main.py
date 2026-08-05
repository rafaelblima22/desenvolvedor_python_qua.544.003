nomes = [
    "Alice",
    "Bernardo",
    "Camila",
    "Daniel",
    "Elena",
    "Felipe",
    "Giovanna",
    "Henrique",
    "Isabela",
    "João",
    "Larissa",
    "Matheus",
    "Beatriz",
    "Rafael",
    "Sofia",
    "Thiago",
    "Valentina",
    "Lucas"
]

nome = input("Informe o nome a se deletado: ").strip().title()

if nome in nomes :
    indice = nomes.index(nome)

    #NOTE - apagar item da lista
    del(nomes[indice])

    #NOTE - exibi a lista sem o nome
    for nome in nomes:
        print(nome)
else:
    print ("Nome não encontrado")