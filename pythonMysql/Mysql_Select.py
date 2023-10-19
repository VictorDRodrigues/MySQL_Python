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

# Passa para variavel que busta cria uma SELECT de alguma tabela exemplo "clientes"
query = '''
    SELECT * FROM clientes
'''
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()

# Retorna um valor de cada CULOUNA do SELECT
columns = tuple([i[0] for i in cursor.description])
print(columns)

# Cria uma loop que mostra cada linha dentro de "result"
for row in result:
  print(row)

