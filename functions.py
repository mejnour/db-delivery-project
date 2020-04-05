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

#Inserir produto
def insertProduct(restaurante ,nome, descricao, categoria):
  #Consulta
  restaurante = restaurante
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    mySql_idSelect_query = "SELECT ID_restaurante FROM Restaurante WHERE Nome = '{}'".format(restaurante)
    cursor = connection.cursor()
    cursor.execute(mySql_idSelect_query)
    records = cursor.fetchall()
    idRestauranteBuscado = int(records[0][0])
    #print(idRestauranteBuscado)

    mySql_cardapioSelect_query = "SELECT ID_cardapio FROM Cardapio WHERE ID_restaurante = {}".format(idRestauranteBuscado)
    cursor.execute(mySql_cardapioSelect_query)
    records = cursor.fetchall()
    idCardapioBuscado = int(records[0][0])
    #print(idCardapioBuscado)
  except mysql.connector.Error as error:
    print("Failed to get record into Restaurante table {}".format(error))

  finally:
    if(connection.is_connected()):
      cursor.close()
      connection.close()
      print("MySQL connection is closed")
  #Insert
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    mySql_insert_query = """INSERT INTO Comida (Nome, Descricao, Categoria, ID_cardapio)
                            VALUES
                            ('{}', '{}', '{}', {})""".format(nome, descricao, categoria, idCardapioBuscado)
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Comida table")
    cursor.close()

  except mysql.connector.Error as error:
    print("Failed to insert record into Comida table {}".format(error))

  finally:
    if(connection.is_connected()):
      connection.close()
      print("MySQL connection is closed")

#Função para mostrar as comidas de um restaurante
def showProductsFromRestaurant(restaurante):
  restaurante = restaurante
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    mySql_idSelect_query = "SELECT ID_restaurante FROM Restaurante WHERE Nome = '{}'".format(restaurante)
    cursor = connection.cursor()
    cursor.execute(mySql_idSelect_query)
    records = cursor.fetchall()
    idRestauranteBuscado = int(records[0][0])
    #print(idRestauranteBuscado)

    mySql_cardapioSelect_query = "SELECT ID_cardapio FROM Cardapio WHERE ID_restaurante = {}".format(idRestauranteBuscado)
    cursor.execute(mySql_cardapioSelect_query)
    records = cursor.fetchall()
    idCardapioBuscado = int(records[0][0])
    #print(idCardapioBuscado)
    
    mySql_contemSelect_query = "SELECT * FROM Contem WHERE ID_cardapio = {}".format(idCardapioBuscado)
    cursor.execute(mySql_contemSelect_query)
    records = cursor.fetchall()
    listaDeIdComidas = []
    for row in records:
      listaDeIdComidas.append(row[1])
    for i in range(len(listaDeIdComidas)):
      mySql_comidaSelect_query = "SELECT * FROM Comida WHERE ID_Comida = {}".format(listaDeIdComidas[i])
      cursor.execute(mySql_comidaSelect_query)
      records = cursor.fetchall()
      for row in records:
        print('\nNome do Produto:', row[1])
        print('Categoria:', row[3])
        print('Descrição:', row[2])        
        mySql_precoSelect_query = "SELECT Valor FROM Preco WHERE ID_Comida = {}".format(listaDeIdComidas[i])
        cursor.execute(mySql_precoSelect_query)
        precoRecords = cursor.fetchall()
        print('Preço: R${}'.format(float(precoRecords[0][0])))
  
  except mysql.connector.Error as error:
    print("Failed to get record into Restaurante table {}".format(error))

  finally:
    if(connection.is_connected()):
      cursor.close()
      connection.close()
      print("MySQL connection is closed")
      return

#Mostra as categorias de comida disponíveis no banco
def showCategories():
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    mySql_categoriaSelect_query = "SELECT Categoria FROM Comida"
    cursor = connection.cursor()
    cursor.execute(mySql_categoriaSelect_query)
    records = cursor.fetchall()
    print('Categorias Disponíveis:')
    for i in range(len(records)):
      print('\n', records[i][0])

  except mysql.connector.Error as error:
    print("Failed to get record into Comida table {}".format(error))

  finally:
    if(connection.is_connected()):
      cursor.close()
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

#Input dos campos necessários para inserir comida TODO: Questão da tabela Contem 
def askProductInformationInput():
  print('Digite o nome do restaurante e os atributos da Tabela \'Comida\'')
  nomeRestaurante = input('Nome do Restaurante que terá essa comida: ')
  nomeComida = input('Nome da comida: ')
  descricao = input('Descrição: ')
  categoria = input('Categoria: ')
  return nomeRestaurante, nomeComida, descricao, categoria

def main():
  op = 1
  while(op != 0):
    print('\nDigite 0 para sair dos testes')
    print('Digite 1 para inserir Usuário')
    print('Digite 2 para inserir Restaurante')
    print('Digite 3 para mostrar comidas de um Restaurante')
    print('Digite 4 para mostrar as categorias de produtos disponíveis')
    print('Digite 5 para inserir um produto em um restaurante')
    op = int(input())
    if (op != 0):
      if(op == 1):
        nome, senha, email, telefone, endereco = askUserInput()
        insertUser(nome, senha, email, telefone, endereco)
      if (op == 2):
        categoria, nome, senha, email, telefone, endereco, tipoDeEntrega = askRestaurantInput()
        insertRestaurant(categoria, nome, senha, email, telefone, endereco, tipoDeEntrega)
      if (op == 3):
        nomeRestaurante = input("Nome do restaurante: ")
        showProductsFromRestaurant(nomeRestaurante)
      if (op == 4):
        showCategories()
      if (op == 5):
        nomeRestaurante, nomeComida, descricao, categoria = askProductInformationInput()
        insertProduct(nomeRestaurante, nomeComida, descricao, categoria) 
  print('Exiting...')

main()

