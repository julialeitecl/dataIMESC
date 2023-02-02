import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='testandoschema',
)
cursor = conexao.cursor()

#### CRUD #####

#CREATE
nome_produto = "xxx"
valor = 3
comando = f'INSERT INTO sales(nome_produto,valor) VALUES ("{nome_produto}","{valor}")'
cursor.execute(comando)
conexao.commit() #quando edita o banco de dados
#resultado = cursor.fetchall() #lendo o banco de dados

#READ
#UPDATE
#DELETE

cursor.close()
conexao.close()