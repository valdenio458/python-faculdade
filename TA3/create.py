import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('code_join.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# CREATE
# Comando SQL para criar a tabela 'customer'
cursor.execute("""
CREATE TABLE customer (
  id int,
  name varchar(30),
  email varchar(30),
  password varchar(30),
  cpf varchar(40),
  renewal_date date,
  code varchar(30)
)
""")

# Commit para salvar as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()






