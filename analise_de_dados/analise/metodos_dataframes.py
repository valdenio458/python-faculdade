import pandas as pd

data = {'Nome': ['Alice', 'Bob', 'Charlie'],
        'Idade': [25, 30, 35],
        'Cidade': ['Nova York', 'Los Angeles', 'Chicago']}

df_dados = pd.DataFrame(data)

print('\nInformações do DataFrame:\n')
print(df_dados.info()) # Apresenta informações sobre a estrutura do DF

print('\nQuantidade de linhas e colunas = ', df_dados.shape) # Retorna uma tupla com o número de linhas e colunas
print('\nTipo de dados:\n', df_dados.dtypes) # Retorna o tipo de dados, para cada coluna, se for misto será object

print('\nQual o menor valor de cada coluna?\n', df_dados.min()) # Extrai o menor de cada coluna 
print('\nQual o maior valor?\n', df_dados.max()) # Extrai o valor máximo e cada coluna 
print('\nQual a média aritmética?\n', df_dados.mean()) # Extrai a média aritmética de cada coluna numérica
print('\nQual o desvio padrão?\n', df_dados.std()) # Extrai o desvio padrão de cada coluna numérica
print('\nQual a mediana?\n', df_dados.median()) # Extrai a mediana de cada coluna numérica

print('\nResumo:\n', df_dados.describe()) # Exibe um resumo

df_dados.head() # Exibe os 5 primeiros registros do DataFrame