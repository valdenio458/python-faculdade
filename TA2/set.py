# Criar um conjunto de números inteiros
numeros = set([1, 2, 3, 4, 5, 1, 2, 3])  # Note que os números duplicados são automaticamente removidos
# Outra forma de criar um conjunto de números inteiros
# numeros = {1, 2, 3, 4,  5, 1, 2, 3}

print(numeros)  # Saída: {1, 2, 3, 4, 5}

# Adicionar um elemento ao conjunto
numeros.add(6)
print(numeros)  # Saída: {1, 2, 3, 4, 5, 6}

# Remover um elemento do conjunto
numeros.remove(3)
print(numeros)  # Saída: {1, 2, 4, 5, 6}

# Verificar se um elemento está no conjunto
print(2 in numeros)  # Saída: True
print(3 in numeros)  # Saída: False
