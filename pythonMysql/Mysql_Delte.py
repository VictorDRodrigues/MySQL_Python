# Importa biblioteca do MYSQL para conexão ao banco de dados.
from mysql.connector import connect

# Cria Função para criar conexão MYSQL ao banco de dados.
def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

# Chama função dando paramentos para conexão ao banco de dados, apontando para utilizar banco de dados especifico.
connection = mysql_connection('localhost', 'victor', 'victor54321', 'dadosaocubo')

query = '''
    DELETE FROM clientes WHERE id = 1007
'''
cursor = connection.cursor()
cursor.execute(query)
connection.commit()