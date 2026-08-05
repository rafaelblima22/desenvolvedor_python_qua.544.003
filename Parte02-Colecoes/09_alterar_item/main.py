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
    "Natália",
    "Otávio",
    "Beatriz",
    "Rafael",
    "Sofia",
    "Thiago",
    "Valentina",
    "Lucas"
]

#NOTE - Usuario informa o nome que deseja alterar
nome_antigo = input("Informe o nome que eseje alterar: ").strip().title()

#NOTE - armazena a posição do nome na lista caso exista 
if nome_antigo in nomes: 
    indice = nomes.index(nome_antigo)

    nomes[indice] = input("Informe o novo nome: ").strip().title()
    print("Nome alterado com sucesso!")
    for nome in nomes:
        print(nome)
else: 
    print("Nome não encontrado!")