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
    INSERT INTO clientes VALUES
        (1001, 'Joãozinho Silva', '7199999-9999', 'joao@email.com', 'Salvador'),
        (1002, 'Paula Silva', '2199999-9999', 'paula@email.com', 'Rio'),
        (1003, 'Patricia Silva', '1199999-9999', 'paty@email.com', 'Sampa'),
        (1004, 'Zé Silva', '4199999-9999', 'ze@email.com', 'Curitiba'),
        (1005, 'Richarlison Pombo', '3199999-9999', 'pombo@email.com', 'Nova Venécia'),
        (1006, 'Vini Junior', '2199999-9999', 'vini@email.com', 'Rio'),
        (1007, 'Neymar Junior', '1199999-9999', 'ney@email.com', 'Santos')
'''
cursor = connection.cursor()
cursor.execute(query)
connection.commit()