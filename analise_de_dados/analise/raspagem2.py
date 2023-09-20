import pandas as pd
# import requests

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

# Esse código não funcionou. A função read_html não encontrou tabelas no endereço especificado.