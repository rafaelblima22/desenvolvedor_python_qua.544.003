# Criando uma lista de números
numeros = [42, 10, 3, 55, 21, 8]
print("Lista:", numeros)

# Ordena a própria lista em memória
numeros.sort()
print("Lista ordenada:", numeros)

#Ordenando em ordem decrescente (do maior para o menor)
numeros.sort(reverse=True)
print("Lista em ordem decrescente:", numeros)

# Cria uma NOVA lista ordenada, mantendo a original intacta
outros_numeros = [15, 2, 89, 4]
lista_ordenada = sorted(outros_numeros)

print("\nOutra lista original:", outros_numeros)
print("Nova lista gerada com sorted():", lista_ordenada)

#Ordena em ordem alfabetica
frutas = ["banana", "maçã", "abacaxi", "laranja"]
frutas.sort()

print("Frutas em ordem alfabética:", frutas)