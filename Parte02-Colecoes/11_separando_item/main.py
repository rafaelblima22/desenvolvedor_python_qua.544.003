nomes = ["Alice","Bernardo","Camila","Daniel","Elena","Felipe","Giovanna","Henrique","Isabela","João","Larissa","Matheus","Beatriz","Rafael","Sofia","Thiago","Valentina","Lucas"]

nome = input("Informe o nome a ser separado: ").strip().title()

if nome in nomes:
    indice = nomes.index(nome)

    #NOTE - separar nome da lista
    nome_separado = nomes.pop(indice)

    #NOTE - exibe a lista
    for nome in nomes:
        print(nome)
    print(f"Nome separado da lista : {nome_separado}")
    
else:
    print("Nome não encontrado.")