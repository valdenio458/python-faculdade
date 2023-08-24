import sqlite3
conn = sqlite3.connect('bank')
print(type(conn))



# ddl_create = """
# CREATE TABLE customer (
#   id int,
#   name varchar(30),
#   email varchar(30),
#   password varchar(30),
#   cpf varchar(40),
#   renewal_date date,
#   code varchar(30)
# )

# """

cursor = conn.cursor()
# cursor.execute(ddl_create)
print(cursor.description)
print(cursor.rowcount)
cursor.close()
conn.close()