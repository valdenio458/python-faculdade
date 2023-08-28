import pandas as pd

nums = pd.Series([10.2, -1, None, 15, 23.4])
print('Menor valor: ', nums.min())
print('Maior valor: ', nums.max())
print('Média: ', nums.mean())
print('Resumo:\n', nums.describe())