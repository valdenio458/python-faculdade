import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('code_join.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Comando SQL para selecionar todos os registros da tabela 'customer'
select_query = """
SELECT * FROM customer
"""

# Executa o comando SQL usando o cursor
cursor.execute(select_query)

result = cursor.fetchall()
for linha in result:
  print(linha)

# Fechar a conexão com o banco de dados
conn.close()