# NOTE - Criando uma lista
paises = [
    "Brasil", 
    "Argentina", 
    "Brasil", 
    "Uruguai",
    "Estados Unidos",
    "Paraguai", 
    "Chile", 
    "Colômbia",
    "Brasil",  
    "Peru", 
    "Equador", 
    "Venezuela",
    "Brasil",  
    "Irã",
    "Japão",
    "Brasil", 
    "México",
    "Estados Unidos"
]

# NOTE - 
pais = input("Informe o país a ser pesquisado: ").strip().title()

#NOTE - Quantidade de vezes que foi encontrado na lista
qtde = paises.count(pais)

print(f"{pais} foi encontrado {qtde} vezes na lista.")