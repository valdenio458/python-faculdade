# Definir uma função simples
def pares(x):
    return x % 2 == 0
    

# Criar uma lista de números
numeros = [1, 2, 3, 4, 5]

# Usar a função map para aplicar a função 'quadrado' a cada número na lista
num_pares = map(pares, numeros)

# Converter o iterador resultante de 'map' de volta para uma lista
num_pares_lista = list(num_pares)

# Imprimir a lista de num_pares
print(num_pares_lista)
