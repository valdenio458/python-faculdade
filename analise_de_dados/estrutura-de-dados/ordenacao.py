lista = [7, 4]

if (lista[0] > lista [1]): 
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)


# Ordenação pythônica (atribuição múltipla)
lista = [-1, 5]

if (lista[0] > lista [1]): 
    lista[0], lista[1] = lista[1], lista[0]

print(lista)