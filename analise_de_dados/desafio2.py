texto = """

A inserção de comentários no código do programa é uma prática normal.
"""
letra = 0
for i, c in enumerate(texto):
    if c == 'a' or c == 'e':
        letra += 1
        print(f"Vogal '{c}' encontrada, na posição {i}")
    else:
        continue
print(f"Quantidade de vogais encontradas: {letra}")