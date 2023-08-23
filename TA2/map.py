# Definir uma função simples
def quadrado(x):
    return x ** 2

# Criar uma lista de números
numeros = [1, 2, 3, 4, 5]

# Usar a função map para aplicar a função 'quadrado' a cada número na lista
quadrados = map(quadrado, numeros)

# Converter o iterador resultante de 'map' de volta para uma lista
quadrados_lista = list(quadrados)

# Imprimir a lista de quadrados
print(quadrados_lista)
