# NOTE - Criando uma lista
elementos = [10, 20, 30, 40, 50]
print("Lista:", elementos)

# Modifica a própria lista em memória
elementos.reverse()
print("Lista invertida:", elementos)


# Cria uma NOVA lista invertida, mantendo a original intacta
original = [1, 2, 3, 4, 5]
invertida_slice = original[::-1]

print("\nLista original:", original)
print("Nova lista invertida:", invertida_slice)


# Retorna um iterador que precisa ser convertido para lista
outra_lista = ["a", "b", "c", "d"]
invertida_iter = list(reversed(outra_lista))

print("\nOutra lista original:", outra_lista)
print("Invertida:", invertida_iter)