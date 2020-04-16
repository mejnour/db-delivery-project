# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime
from collections import Counter


#Função para mostrar todo histórico de um usuário
def clientOrderHistory(nomeDoUsuario):
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    
    mySql_idUsuarioSelect_query = "SELECT ID_Usuario FROM Usuario WHERE Nome = '{}'".format(nomeDoUsuario)
    cursor = connection.cursor()
    cursor.execute(mySql_idUsuarioSelect_query)
    records = cursor.fetchall()
    idUsuarioBuscado = int(records[0][0])
    
    mySql_clientHistorySelect_query = """SELECT Pedido.Data_hora, Pedido.Local_de_entrega, Pedido.ID_restaurante, Pedido.ID_pedido 
                                         From Pedido 
                                         INNER JOIN Usuario ON Usuario.ID_Usuario = {} 
                                         ORDER BY Data_Hora DESC""".format(idUsuarioBuscado)
    cursor = connection.cursor()
    cursor.execute(mySql_clientHistorySelect_query)
    records = cursor.fetchall()
    #print(records)

    for row in records:
      idRestaurante = int(row[2])
      
      mySql_restauranteNameSelect_query = "SELECT Nome FROM Restaurante WHERE ID_restaurante = {}".format(idRestaurante)
      cursor = connection.cursor()
      cursor.execute(mySql_restauranteNameSelect_query)
      recordsNomeRestaurante = cursor.fetchall()
      
      print('\nPedido feito em:', str(recordsNomeRestaurante[0][0]))
      print('Local entregado:', row[1])
      print('Data:', row[0])


  except mysql.connector.Error as error:
    print("Failed to get record from Pedidos table {}".format(error))

  finally:
    if(connection.is_connected()):
      connection.close()
      print("MySQL connection is closed")
    
#Insert do Usuario
def insertUser(nome, senha, email, telefone, endereco):
  #Inicialmente os parâmetros estão assim, mas podem ser modificados para ficar em outro estilo(receber tuplas ou objetos)
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
    mySql_restauranteInsert_query = """INSERT INTO Restaurante (Categoria, Nome, Senha, Email, Telefone, Endereco_, Entrega_rapida, Entrega_gratis)
                            VALUES
                            ('{}', '{}', '{}', '{}', '{}', '{}', {}, {})""".format(categoria, nome, senha, email, telefone, endereco, entrega_rapida, entrega_gratis)
    cursor = connection.cursor()
    cursor.execute(mySql_restauranteInsert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Restaurante table")
    cursor.close()

    mySql_idSelect_query = "SELECT ID_restaurante FROM Restaurante WHERE Nome = '{}'".format(nome)
    cursor = connection.cursor()
    cursor.execute(mySql_idSelect_query)
    records = cursor.fetchall()
    idRestauranteBuscado = int(records[0][0])
    #print(idRestauranteBuscado)

    nomeDoCardapio = nome + '_Cardapio'
    mySql_cardapioInsert_query = """INSERT INTO Cardapio (Nome_cardapio, ID_restaurante)
                            VALUES
                            ('{}', {})""".format(nomeDoCardapio, idRestauranteBuscado)
    cursor = connection.cursor()
    cursor.execute(mySql_cardapioInsert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Cardapio table")
    cursor.close()

  except mysql.connector.Error as error:
    print("Failed to insert record into Restaurante table {}".format(error))

  finally:
    if(connection.is_connected()):
      connection.close()
      print("MySQL connection is closed")

#Inserir produto
def insertProduct(restaurante ,nome, descricao, categoria, preco):
  #Consulta
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
    mySql_insert_query = """INSERT INTO Comida (Nome, Descricao, ID_cardapio, Categoria)
                            VALUES
                            ('{}', '{}', {}, '{}')""".format(nome, descricao, idCardapioBuscado, categoria)
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Comida table")
    cursor.close()

    mySql_idComidaSelect_query = "SELECT ID_Comida FROM Comida WHERE Nome = '{}'".format(nome)
    cursor = connection.cursor()
    cursor.execute(mySql_idComidaSelect_query)
    records = cursor.fetchall()
    idDaComidaInserida = records[0][0]
    #print(idDaComidaInserida)
    dataDeRegistroComida = datetime.datetime.now()
    formattedDate = dataDeRegistroComida.strftime('%Y-%m-%d %H:%M:%S')
    #print(formattedDate)
    #print(type(formattedDate))

    mySql_contemInsert_query = """INSERT INTO Contem (ID_cardapio, ID_Comida)
                                  VALUES
                                  ({}, {})""".format(idCardapioBuscado, idDaComidaInserida)
    cursor = connection.cursor()
    cursor.execute(mySql_contemInsert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Contem table")
    cursor.close()   

    mySql_precoInsert_query = """INSERT INTO Preco (Valor, Data_hora, ID_Comida)
                                 VALUES
                                 ({}, '{}', {})""".format(preco, formattedDate, idDaComidaInserida)
    cursor = connection.cursor()
    cursor.execute(mySql_precoInsert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Preco table")
    cursor.close() 

  except mysql.connector.Error as error:
    print("Failed to insert record into Comida table {}".format(error))

  finally:
    if(connection.is_connected()):
      connection.close()
      print("MySQL connection is closed")

#Função de inserir na tabela Pedido
def insertPedido(nomeUsuario, nomeRestaurante, enderecoDeEntrega, listaDeIdComidas):
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    
    mySql_idRestauranteSelect_query = "SELECT ID_restaurante FROM Restaurante WHERE Nome = '{}'".format(nomeRestaurante)
    cursor = connection.cursor()
    cursor.execute(mySql_idRestauranteSelect_query)
    records = cursor.fetchall()
    idRestauranteBuscado = int(records[0][0])
    #print(idRestauranteBuscado)

    mySql_idUsuarioSelect_query = "SELECT ID_Usuario FROM Usuario WHERE Nome = '{}'".format(nomeUsuario)
    cursor = connection.cursor()
    cursor.execute(mySql_idUsuarioSelect_query)
    records = cursor.fetchall()
    idUsuarioBuscado = int(records[0][0])
    #print(idRestauranteBuscado)
    
    dataDePedidoFeito = datetime.datetime.now()
    formattedDate = dataDePedidoFeito.strftime('%Y-%m-%d %H:%M:%S')

    mySql_pedidoInsert_query = """INSERT INTO Pedido (Data_hora, ID_restaurante, ID_Usuario, Local_de_entrega)
                                  VALUES
                                  ('{}', {}, {}, '{}')""".format(formattedDate, idRestauranteBuscado, idUsuarioBuscado, enderecoDeEntrega)
    cursor = connection.cursor()
    cursor.execute(mySql_pedidoInsert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Pedido table")
    cursor.close()

  except mysql.connector.Error as error:
    print("Failed to insert record into Pedido table {}".format(error))

  finally:
    if(connection.is_connected()):
      connection.close()
      print("MySQL connection is closed")
  
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    
    mySql_idPedidoSelect_query = "SELECT ID_pedido FROM Pedido WHERE ID_Usuario = {} AND Data_hora = '{}'".format(idUsuarioBuscado, formattedDate)
    cursor = connection.cursor()
    cursor.execute(mySql_idPedidoSelect_query)
    records = cursor.fetchall()
    idPedidoFeito = int(records[0][0])
    #print(idRestauranteBuscado)
    
    for i in range(len(listaDeIdComidas)):
      idComidaAtual = int(listaDeIdComidas[i])
      mySql_pedidoContemComidaInsert_query = """INSERT INTO PedidoContemComida (ID_pedido, ID_Comida)
                                                VALUES
                                                ({}, {})""".format(idPedidoFeito, idComidaAtual)
      cursor = connection.cursor()
      cursor.execute(mySql_pedidoContemComidaInsert_query)
      connection.commit()
      print(cursor.rowcount, "Record inserted successfully into PedidoContemComida table")
      cursor.close()

  except mysql.connector.Error as error:
    print("Failed to insert record into PedidoContemComida table {}".format(error))

  finally:
    if(connection.is_connected()):
      connection.close()
      print("MySQL connection is closed")

#Função para deletar produto das tabelas Preco, Contem e Comida utilizando nome do restaurante e do produto
def deleteProduct(nomeDoRestaurante,nomeDaComida):
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                        user="SKdTbdX8lK",
                                        passwd="yODtLD4Q0z",
                                        database='SKdTbdX8lK')

    mySql_idRestauranteSelect_query = "SELECT ID_restaurante FROM Restaurante WHERE Nome = '{}'".format(nomeDoRestaurante)
    cursor = connection.cursor()
    cursor.execute(mySql_idRestauranteSelect_query)
    records = cursor.fetchall()
    idRestauranteBuscado = int(records[0][0])

    mySql_idCardapioSelect_query = "SELECT ID_cardapio FROM Cardapio WHERE ID_restaurante = {}".format(idRestauranteBuscado)
    cursor.execute(mySql_idCardapioSelect_query)
    records = cursor.fetchall()
    idCardapioBuscado = int(records[0][0])

    mySql_idComidaSelect_query = "SELECT ID_Comida FROM Comida WHERE Nome = '{}' AND ID_cardapio = {}".format(nomeDaComida , idCardapioBuscado)
    cursor.execute(mySql_idComidaSelect_query)
    records = cursor.fetchall()
    idComidaBuscado = int(records[0][0])

    deletePrecoQuery = "DELETE FROM Preco WHERE ID_Comida = {}".format(idComidaBuscado)
    deleteContemQuery = "DELETE FROM Contem WHERE ID_Comida = {}".format(idComidaBuscado) 
    deleteComidaQuery = "DELETE FROM Comida WHERE ID_Comida = {}".format(idComidaBuscado)

    cursor = connection.cursor()
    
    cursor.execute(deletePrecoQuery)
    connection.commit()
    cursor.execute(deleteContemQuery)
    connection.commit()
    cursor.execute(deleteComidaQuery)
    connection.commit()
    
    print(cursor.rowcount, "Record deleted successfully from Comida table")
    cursor.close()

  except mysql.connector.Error as error:
    print("Failed to delete record from table: {}".format(error))

  finally:
    if (connection.is_connected()):
      connection.close()
      print("MySQL connection is closed")

#Retorna o preço médio de cada comida vendida nos 7 dias anteriores
def showProductAverageHistory(nomeDoRestaurante):
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    mySql_idRestauranteSelect_query = "SELECT ID_restaurante FROM Restaurante WHERE Nome = '{}'".format(nomeDoRestaurante)
    cursor = connection.cursor()
    cursor.execute(mySql_idRestauranteSelect_query)
    records = cursor.fetchall()
    idRestauranteBuscado = int(records[0][0])

    mySql_idCardapioSelect_query = "SELECT ID_cardapio FROM Cardapio WHERE ID_restaurante = {}".format(idRestauranteBuscado)
    cursor.execute(mySql_idCardapioSelect_query)
    records = cursor.fetchall()
    idCardapioBuscado = int(records[0][0])

    mySql_averageProductSelect_query = """SELECT AVG(Preco.Valor), Preco.ID_Comida, Cardapio.ID_restaurante FROM Preco 
                                          INNER JOIN Comida ON Preco.ID_Comida = Comida.ID_Comida INNER JOIN Cardapio ON Comida.ID_cardapio = {} 
                                          WHERE Preco.Data_hora >= DATE_ADD(CURRENT_DATE(),INTERVAL -7 DAY) AND Cardapio.ID_restaurante = {}
                                          GROUP BY Preco.ID_Comida""".format(idCardapioBuscado, idRestauranteBuscado)
    cursor.execute(mySql_averageProductSelect_query)
    records = cursor.fetchall()
    #print(records)

    for row in records:
      idAtual = row[1]
      mySql_comidaNameSelect_query = "SELECT Nome FROM Comida WHERE ID_Comida = {}".format(idAtual)
      cursor = connection.cursor()
      cursor.execute(mySql_comidaNameSelect_query)
      recordsNomeComida = cursor.fetchall()
      print('Nome da comida:', str(recordsNomeComida[0][0]))
      print('Preço médio da comida nos últimos 7 dias: R$ %.2f' % row[0])


  except mysql.connector.Error as error:
    print("Failed to get record into Restaurante table {}".format(error))
  
  finally:
    if(connection.is_connected()):
      cursor.close()
      connection.close()
      print("MySQL connection is closed")

#Função para mostrar as comidas de um restaurante
def showProductsFromRestaurant(restaurante):

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
        print('Categoria:', row[4])
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

      #Mostra a comida com a maior quantidade de pedidos

#Função para mostrar comida mais pedida
def showBestSellingProduct(nomeDoRestaurante):

  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    
    mySql_idRestauranteSelect_query = "SELECT ID_restaurante FROM Restaurante WHERE Nome = '{}'".format(nomeDoRestaurante)
    cursor = connection.cursor()
    cursor.execute(mySql_idRestauranteSelect_query)
    records = cursor.fetchall()
    idRestauranteBuscado = int(records[0][0])

    mySql_bestSellingSelect_query = """SELECT r.nome as Restaurante, c.Nome, COUNT(*) as quantity FROM Restaurante r JOIN Pedido p ON r.ID_Restaurante = p.ID_Restaurante JOIN PedidoContemComida pc ON pc.ID_Pedido = p.ID_Pedido JOIN Comida c ON pc.ID_Comida = c.ID_Comida
                                       WHERE r.ID_Restaurante = {}
                                       GROUP BY Restaurante, c.Nome
                                       ORDER BY quantity DESC
                                       LIMIT 1""".format(idRestauranteBuscado)
    cursor = connection.cursor()
    cursor.execute(mySql_bestSellingSelect_query)
    records = cursor.fetchall()
    #print(records)
    for row in records:
      #print('Nome do restaurante:', row[0])
      print('Nome da comida:', row[1])
      print('Quantidade Vendida no total:', row[2])
  
  except mysql.connector.Error as error:
    print("Failed to get record into PedidoContemComida table {}".format(error))
    
  finally:
    if(connection.is_connected()):
      cursor.close()
      connection.close()
      print("MySQL connection is closed")

#TODO Ao selecionar comida, retornar restaurantes que vendem
def showRestaurantsWithProduct(comida):
  try:
    connection = mysql.connector.connect(host='remotemysql.com',
                                         user="SKdTbdX8lK",
                                         passwd="yODtLD4Q0z",
                                         database='SKdTbdX8lK')
    mySql_idSelect_query = "SELECT ID_Comida FROM Comida WHERE Nome = '{}'".format(comida)
    cursor = connection.cursor()
    cursor.execute(mySql_idSelect_query)
    records = cursor.fetchall()
    idComidaBuscado = int(records[0][0])
    #print(idComidaBuscado)

    mySql_contemSelect_query = "SELECT * FROM Contem WHERE ID_Comida = {}".format(idComidaBuscado)
    cursor = connection.cursor()
    cursor.execute(mySql_contemSelect_query)
    records = cursor.fetchall()
    listaDeIdCardapios = []
    for row in records:
      #print(row[0])
      listaDeIdCardapios.append(row[0])
    for i in range(len(listaDeIdCardapios)):
      mySql_IDrestauranteSelect_query = "SELECT * FROM Cardapio WHERE ID_cardapio = {}".format(listaDeIdCardapios[i])
      cursor.execute(mySql_IDrestauranteSelect_query)
      recordsCardapio = cursor.fetchall()
      listadeIdRestaurantes = []
      for row in recordsCardapio:
        #print(row[2])
        listadeIdRestaurantes.append(row[2])
      for j in range(len(listadeIdRestaurantes)):
        mySql_restauranteSelect_query = "SELECT * FROM Restaurante WHERE ID_restaurante = {}".format(listadeIdRestaurantes[j])
        cursor.execute(mySql_restauranteSelect_query)
        recordsRestaurante = cursor.fetchall()
        for row in recordsRestaurante:
          print('\nNome do Restaurante:', row[2])

  except mysql.connector.Error as error:
    print("Failed to get record into Contem table {}".format(error))

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

    # array auxiliar usado para limitar
    # a quantidade de categorias, mostrando
    # apenas uma de cada.
    show_only = []

    for i in range(len(records)):
      if records[i][0] not in show_only: # teste se a entrada já está no array
        show_only.append(records[i][0])
        # print(show_only)
        print('\n', records[i][0])
    print('\n')

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
  preco = input('Preço: ')
  return nomeRestaurante, nomeComida, descricao, categoria, preco

def askProductInfoForDeletion():
  print('\nDigite o nome dos atributos do produto que você quer deletar')
  nomeRestaurante = input('Nome do restaurante que tem a comida: ')
  nomeComida = input('Nome da comida a ser deletada: ')
  return nomeRestaurante, nomeComida

def main():
  op = 1
  while(op != 0):
    print('\nDigite 0 para sair dos testes')
    print('Digite 1 para inserir Usuário')
    print('Digite 2 para inserir Restaurante')
    print('Digite 3 para mostrar comidas de um Restaurante')
    print('Digite 4 para mostrar as categorias de produtos disponíveis')
    print('Digite 5 para inserir um produto em um restaurante')
    print('Digite 6 para procurar restaurantes com a comida passada')
    print('Digite 7 para deletar um produto de um restaurante específico')
    print('Digite 8 para mostrar um histórico dos preços médios das comidas de um restaurante específico')
    print('Digite 9 para motrar a lista do produto mais vendido')
    print('Digite 10 para motrar o histórico de pedidos de um usuário')

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
        nomeRestaurante, nomeComida, descricao, categoria, preco= askProductInformationInput()
        insertProduct(nomeRestaurante, nomeComida, descricao, categoria, preco)
      if (op == 6):
        nomeDaComida = input("Digite o nome da comida que quer procurar: ")
        showRestaurantsWithProduct(nomeDaComida)
      if (op == 7):
        nomeDoRestaurante, nomeDaComida = askProductInfoForDeletion()
        deleteProduct(nomeDoRestaurante, nomeDaComida)
      if (op == 8):
        nomeDoRestaurante = input('Nome do restaurante: ')
        showProductAverageHistory(nomeDoRestaurante)
      if (op == 9):
        nomeDoRestaurante = input ('Nome do restaurante: ')
        showBestSellingProduct(nomeDoRestaurante)  
      if (op == 10):
        nomeDoUsuario = input('Nome do Usuário: ')
        clientOrderHistory(nomeDoUsuario)

  print('Exiting...')

def testeInsertPedido():
  nomeDoUsuario = 'Jill Valentine'
  nomeDoRestaurante = 'Habibs'
  enderecoDeEntrega = '1250 W South St, Raccon City'
  listaDeIdComidas = [25]
  
  insertPedido(nomeDoUsuario, nomeDoRestaurante, enderecoDeEntrega, listaDeIdComidas)

def most_frequent(List):
  occurence_count = Counter(List) 
  return occurence_count.most_common(1)[0][0]

if __name__ == "__main__":
  main()

#testeInsertPedido()