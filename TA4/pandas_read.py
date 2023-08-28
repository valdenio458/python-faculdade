import pandas as pd 

url = 'https://en.wikipedia.org/wiki/Minnesota'

dfs = pd.read_html(url)
print(type(dfs))
print(len(dfs))
