import pandas as pd

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

print(pd.DataFrame(lista_nomes, columns=['Nome']))

print(pd.DataFrame(lista_nomes, columns=['Nome'], index=lista_cpfs))


dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas

print(pd.DataFrame(dados, columns=['Nome', 'CPFs', 'Idade', 'e-mail']))