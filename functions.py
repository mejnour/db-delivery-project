import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


#Insert do Usuario
def insertUser(nome, senha, email, telefone, endereco):
  #Inicialmente os parâmetros estão assim, mas podem ser modificados para ficar em outro estilo(receber tuplas ou objetos)
  nome = nome
  senha = senha
  email = email
  telefone = telefone
  endereco = endereco
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    mySql_insert_query = """INSERT INTO Usuario (Nome, Senha, Email, Telefone, Endereco)
                            VALUES
                            ('{}', '{}', '{}', '{}', '{}')""".format(nome, senha, email, telefone, endereco)
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Usuario table")
    cursor.close()

  except mysql.connector.Error as error:
    print("Failed to insert record into Usuario table {}".format(error))

  finally:
    if(connection.is_connected()):
      connection.close()
      print("MySQL connection is closed")

#Insert do Restaurante
def insertRestaurant(categoria, nome, senha, email, telefone, endereco, tipoDeEntrega):
  #Inicialmente os parâmetros estão assim, mas podem ser modificados para ficar em outro estilo(receber tuplas ou objetos)
  #Mudar na Database a tipagem dos atributos Entrega_rapida e Entrega_gratis de decimal para outro mais apropriado. 
  #Por enquanto aqui estarei colocando na condicional levando em consideração do tipo como decimal desses campos
  categoria = categoria
  nome = nome
  senha = senha
  email = email
  telefone = telefone
  endereco = endereco
  if (tipoDeEntrega == 'rapida'):
    entrega_gratis = 0
    entrega_rapida = 1
  else:
    entrega_gratis = 1
    entrega_rapida = 0
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    mySql_insert_query = """INSERT INTO Restaurante (Categoria, Nome, Senha, Email, Telefone, Endereco_, Entrega_rapida, Entrega_gratis)
                            VALUES
                            ('{}', '{}', '{}', '{}', '{}', '{}', {}, {})""".format(categoria, nome, senha, email, telefone, endereco, entrega_rapida, entrega_gratis)
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Restaurante table")
    cursor.close()

  except mysql.connector.Error as error:
    print("Failed to insert record into Restaurante table {}".format(error))

  finally:
    if(connection.is_connected()):
      connection.close()
      print("MySQL connection is closed")

#Função só para testar os inserts via input(), alterar de acordo com a tabela
def askUserInput():
  print('Digite os atributos da Tabela \'Usuario\'')
  nome = input('Nome: ')
  senha = input('Senha: ')
  email = input('Email: ')
  telefone = input('Telefone: ')
  endereco = input('Endereço: ')
  return nome, senha, email, telefone, endereco

#Mesmo de antes só que com o campos da tabela Restaurante
def askRestaurantInput():
  print('Digite os atributos da Tabela \'Restaurante\'')
  categoria = input('Categoria: ')
  nome = input('Nome: ')
  senha = input('Senha: ')
  email = input('Email: ')
  telefone = input('Telefone: ')
  endereco = input('Endereço: ')
  tipoDeEntrega = input('Tipo da entrega: ')
  return categoria, nome, senha, email, telefone, endereco, tipoDeEntrega

def main():
  op = 1
  while(op != 0):
    print('Digite 0 para sair dos testes')
    print('Digite 1 para inserir Usuário')
    print('Digite 2 para inserir Restaurante')
    op = int(input())
    if (op != 0):
      if(op == 1):
        nome, senha, email, telefone, endereco = askUserInput()
        insertUser(nome, senha, email, telefone, endereco)
      if (op == 2):
        categoria, nome, senha, email, telefone, endereco, tipoDeEntrega = askRestaurantInput()
        insertRestaurant(categoria, nome, senha, email, telefone, endereco, tipoDeEntrega)
  print('Exiting...')

main()

