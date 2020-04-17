#!-*- coding: utf8 -*-

import functions as fn

def fazPedido(carrinho, userEmail):
    idList = []
    while 1:
        print('- - - - - - - - - - - -')
        print('F A Z E R   P E D I D O')    
        print('- - - - - - - - - - - -')

        endereco = input('Entre com um endereco para entrega:\n> ')

        for i in carrinho[1]:
            idList.append(fn.nameProdNameRestaur(carrinho[0], i))

        fn.insertPedido(userEmail, carrinho[0], endereco, idList)

def mostraCarrinho(carrinho):
    print('- - - - - - - -')
    print('C A R R I N H O')    
    print('- - - - - - - -')

    print('Restaurante: {}'.format(carrinho[0]))
    for i in carrinho[1]:
        print('\t\t', i)

    print('\n')

def rmCarrinho(carrinhoLista, rmItem):
    pass

def addCarrinho(carrinhoLista):
    while 1:
        print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
        print('A D I C I O N A R   I T E M   A O   C A R R I N H O')    
        print('- - - - - - - - - - - - - - - - - - - - - - - - - -')

        print('Que item deve ser adicionar ao carrinho?')
        nameRest = input('Nome do restaurante:\n> ')
        nameFoodId = input('Nome da comida:\n> ')

        carrinhoLista.append(nameFoodId)

        return (nameRest, carrinhoLista), carrinhoLista

def gerenteDeItems(userEmail):
    while 1:
        print('- - - - - - - - - - - - - - - - - - - -')
        print('A D I C I O N A R   O U   R E M O V E R')
        print('- - - - - - - - - - - - - - - - - - - -')

        print('Digite 0 para voltar')
        print('Digite 1 para adicionar um item')
        print('Digite 2 para deletar um item')
        print('Digite 3 para mostrar os items deste restaurante')

        try:
            optionGeren = int(input('> '))
        except:
            print('Entrada inválida.')
            print('A entrada deve ser um número!')
            print('Tente novamente.')
    
        print('\n')

        if optionGeren is 1:
            nomeDaComida = input('Entre com o nome do item a ser inserido:\n> ')
            descricaoComida = input('Entre com a descricao do item a ser inserido:\n> ')
            categoriaComida = input('Entre com a categoria do item a ser inserido:\n> ')
            precoComida = input('Entre com o preco do item a ser inserido:\n> ')
            fn.insertProduct(userEmail, nomeDaComida, descricaoComida, categoriaComida, precoComida)
        elif optionGeren is 2:
            nomeDaComida = input('Entre o nome do item a ser deletado:\n> ')
            fn.deleteProduct(nomeDaComida, userEmail)
        elif optionGeren is 3:
            fn.showProductsFromRestaurant(None, userEmail)
        elif optionGeren is 0:
            break
        else:
            print('Entrada inválida. Tente novamente.')
            continue

def relatorios(usuarioEmail):
    while 1:
        print('- - - - - - - - - -')
        print('R E L A T O R I O S')
        print('- - - - - - - - - -')

        print('Digite 0 para voltar')
        print('Digite 1 para mostrar o produto mais vendido')
        print('Digite 2 para mostrar o preço medio praticado pelo restaurante')

        try:
            optionRel = int(input('> '))
        except:
            print('Entrada inválida.')
            print('A entrada deve ser um número!')
            print('Tente novamente.')
    
        print('\n')

        if optionRel is 1:
            fn.showBestSellingProduct(usuarioEmail)
        elif optionRel is 2:
            fn.showProductAverageHistory(usuarioEmail)
        elif optionRel is 0:
            break
        else:
            print('Entrada inválida. Tente novamente.')
            continue


def historico(usuarioEmail):

    '''
    Esta função é responsável por exibir o historico do usuário.
    '''
   
    print('- - - - - - - - - - - - - - - - - - - -')
    print('H I S T O R I C O   D E   P E D I D O S')
    print('- - - - - - - - - - - - - - - - - - - -')
    fn.clientOrderHistory(usuarioEmail)


def pesquisar(carrinho = None, logged = False):

    '''
    Esta função é responsável pesquisar por restaurantes, comidas
    e categorias.
    '''

    categoria = None
    restaurante = None
    comida = None
    optionPesq = None
    
    if carrinho is None:
        carrinhoLista = []
    elif carrinho is not None:
        carrinhoLista = carrinho[1]

    while 1:
        print('- - - - - - - - - - - - - -')
        print('M E N U   P E S Q U I S A R')
        print('- - - - - - - - - - - - - -')
        print('O que voce gostaria de pesquisar?')
        print('Digite 0 para voltar')
        print('Digite 1 para pesquisar por restaurante')
        print('Digite 2 para pesquisar por comida')
        print('Digite 3 para mostrar as categorias')

        if logged is True:
            print('Digite 4 para adicionar item ao carrinho')
            print('Digite 5 para excluir item do carrinho')
        
        try:
            optionPesq = int(input('> '))
        except:
            print('Entrada inválida.')
            print('A entrada deve ser um número!')
            print('Tente novamente.')

        print('\n')

        if optionPesq is 1:
            restaurante = input('Nome do restaurante:\n> ')
            fn.showProductsFromRestaurant(restaurante)
        elif optionPesq is 2:
            comida = input('Nome da comida:\n> ')
            fn.showRestaurantsWithProduct(comida)
        elif optionPesq is 3:
            # categoria = input('Nome da categoria:\n> ')
            fn.showCategories()
        elif optionPesq is 4:
            carrinho, carrinhoLista = addCarrinho(carrinhoLista)
            print(carrinho[1])
        elif optionPesq is 5:
            rmItem = input('Que item voce deseja remover?\n> ')
            rmCarrinho(carrinho, rmItem)
        elif optionPesq is 0:
            break
        else:
            print('Entrada inválida. Tente novamente.')
            continue

    if carrinho is not None:
            return carrinho

def autentica():
    
    '''
    Esta função é responsável pela autenticação dos usuários.
    '''

    isRestaurant = False
    userEmail = None
    userPass = None
    while 1:
        print('- - - - - - - - - - - -')
        print('A U T E N T I C A C A O')
        print('- - - - - - - - - - - -')

        print('Entre com seu e-mail ou digite 0 para voltar:')
        userEmail = input('> ')
        if userEmail is '0':
            print('\n')
            break
        print('Entre com sua senha:')
        userPass = input('> ')

        print('\n')

        try:
            authUser = fn.loginUsuario(userEmail, userPass)
        except:
            pass

        try:
            authRest = fn.loginRestaurante(userEmail, userPass)
        except:
            pass

        if authUser is True:
            print('Autenticação feita com sucesso!')
            isRestaurant = False
            return userEmail, isRestaurant
        elif authRest is True:
            print('Autenticação feita com sucesso!')
            isRestaurant = True
            return userEmail, isRestaurant
        else:
            continue

        break

def cadastro():

    '''
    Esta é a função responsável pelo cadastro de usuários
    e restaurantes.
    '''
    optionCad = None
    
    print('- - - - - - - - - - - - -')
    print('M E N U   C A D A S T R O')
    print('- - - - - - - - - - - - -')

    while 1:
        print('Digite 0 para voltar')
        print('Digite 1 para cadastrar um usuário')
        print('Digite 2 para cadastrar um restaurante')

        optionCad = int(input('> '))

        print('\n')

        if optionCad is 1:
            nome, senha, email, telefone, endereco = fn.askUserInput()
            fn.insertUser(nome, senha, email, telefone, endereco)
            break
        elif optionCad is 2:
            categoria, nome, senha, email, telefone, endereco, tipoDeEntrega = fn.askRestaurantInput()
            fn.insertRestaurant(categoria, nome, senha, email, telefone, endereco, tipoDeEntrega)
            break
        elif optionCad is 0:
            break
        else:
            print('Opção inválida. Tente novamente.')
            continue

def mainCLI():

    '''
    Esta é a main da parte gráfica. Ela é responsável por exibir
    o menu inicial ao usuário e controlar o fluxo do programa de
    acordo.
    '''

    print('\t \t Bem-vindo ao iDOOM')
    print('- The only one that rips and tears your hunger! -')

    loggedEmail = None
    isRest = None
    option = None
    carrinho = None
    logged = None
    while 1:
        print('- - - - - - - - - - - -')
        print('M E N U   I N I C I A L')
        print('- - - - - - - - - - - -')
        print('Digite 0 para sair do iDOOM')

        if loggedEmail is None:
            print('Digite 1 para cadastrar-se')
            print('Digite 2 para entrar')
        
        print('Digite 3 para pesquisar')

        if isRest is False:
            print('Digite 4 para consultar o histórico de pedidos')
        elif isRest is True:
            print('Digite 4 para relatorios')
        
        if isRest is False:
            print('Digite 5 para ver o carrinho')
        elif isRest is True:
            print('Digite 5 para adicionar ou excluir um item')

        if isRest is False:
            print('Digite 6 para fechar o carrinho')

        try:
            option = int(input('> '))
        except:
            print('Entrada inválida.')
            print('A entrada deve ser um número!')
            print('Tente novamente.')
            continue

        print('\n')

        # Cadastra novo usuario
        if loggedEmail is None and option is 1:
            cadastro()
        # Autentica usuario cadastrado
        elif option is 2:
            loggedEmail, isRest = autentica()
            if loggedEmail is not None:
                logged = True
        # Pesquisa por Restaurante, Comida ou Categoria
        elif option is 3:
            carrinho = pesquisar(carrinho, logged)
        # Mostra o historico de pedidos do usuário            
        elif option is 4 and isRest is False:
            historico(loggedEmail)
        # Mostra relatórios do restaurante
        elif option is 4 and isRest is True:
            relatorios(loggedEmail)
        # Insere/Deleta pedido de restaurante
        elif option is 5 and isRest is True:
            gerenteDeItems(loggedEmail)
        # Mostra o carrinho do usuario cliente
        elif option is 5 and isRest is False:
            mostraCarrinho(carrinho)
        # Insere pedido de usuario
        elif option is 6 and isRest is False:
            fazPedido(carrinho, loggedEmail)
        # Sai do aplicativo
        elif option is 0:
            print('Fechando iDOOM...')
            break
        else:
            print('Entrada inválida. Tente novamente')
            continue


if __name__ == '__main__':
    mainCLI()
