# Em Python, as listas podem ser construídas de várias maneiras:

# Usando um par de colchetes para denotar uma lista vazia: lista1 = []
# Usando um par de colchetes e elementos separados por vírgulas: lista2 = ['a', 'b', 'c']
# Usando uma "list comprehension": [x for x in iterable]
# Usando o construtor de tipo: list()

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]

print("Antes da listcomp = ", linguagens)

linguagens_java = [item for item in linguagens if 'Java' in item]

print("\nDepois da listcomp = ", linguagens_java)