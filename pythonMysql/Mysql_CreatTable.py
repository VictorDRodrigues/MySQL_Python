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


# passa comando para variavel que "Cria Tabela de dados dentro do Banco de dados informado no connection".
query = '''
    CREATE TABLE clientes (
        id       INT PRIMARY KEY, 
        nome     VARCHAR(100),
        telefone VARCHAR(15),
        email    VARCHAR(100),
        cidade   VARCHAR(50)
    )
'''
cursor = connection.cursor()
cursor.execute(query)



