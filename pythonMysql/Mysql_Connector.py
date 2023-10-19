# Importa biblioteca do MYSQL para conexão ao banco de dados
from mysql.connector import connect

# Cria Função para criar conexão MYSQL ao banco de dados
def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

# Chama função dando paramentos para conexão ao banco de dados
connection = mysql_connection('localhost', 'victor', 'victor54321')

# Passa paramentro SQL para conex]ao ao Banco de DADOS
query = '''
    create schema if not exists dadosaocubo
'''
# Passa parametro de cruso ao banco de dados
cursor = connection.cursor()
# Passa para o Curso, e manda execursa comando passado para a variavel "query"
cursor.execute(query)

# Finaliza Conexão ao banco de dados
connection.close()
