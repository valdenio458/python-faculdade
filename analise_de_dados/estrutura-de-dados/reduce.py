# Importa a função reduce pois ela não é nativa
from functools import reduce


# Cria um iterável
num = [1, 2, 3, 4]

# Cria a função para somar
def sum(x, y): 
  return x + y

# Cria a função para multiplicar
def multiply(x, y): 
  return x * y

# Aplica o reduce  à soma
res_sum = reduce(sum, num)
print(res_sum)

# Aplica o reduce à multiplicação
res_multiply = reduce(multiply, num)
print(res_multiply)