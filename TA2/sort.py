lista = [10, 4, 1, 15, -3]

lista1 = sorted(lista)  # Cria uma nova lista ordenada
lista2 = lista.sort()   # Ordena a lista original e retorna None

print(lista1)  # Imprime a nova lista ordenada
print(lista2)  # Imprime None, porque o método sort() não retorna nada
print(lista)   # Imprime a lista original, que foi ordenada in-place
