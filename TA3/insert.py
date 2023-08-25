import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('code_join.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# INSERT
# Comando SQL para inserir um novo registro na tabela 'customer'
cursor.execute("""
INSERT INTO customer (
  id,
  name,
  email,
  password,
  cpf ,
  renewal_date ,
  code
)
VALUES(1, 'Seresta Entre Rios', 'codejoin.dev@gmail.com', 'SEREST@2023', 13472070668, '2024-08-24', 'NERES8')
""")

# Commit para salvar as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()







