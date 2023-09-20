import pandas as pd 

# print(pd.Series(data=5))

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
# print(pd.Series(lista_nomes))

dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}

# print(pd.Series(dados))

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
# print(pd.Series(lista_nomes,index=cpfs))

serie_dados = pd.Series(lista_nomes,index=cpfs)
print(serie_dados.loc['222.222.222-22'])