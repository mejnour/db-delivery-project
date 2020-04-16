import functions as fn

def pesquisar():
    categoria = None
    restaurante = None
    comida = None
    optionPesq = None
    while 1:
        print('- - - - - - - - - - - - - -')
        print('M E N U   P E S Q U I S A R')
        print('- - - - - - - - - - - - - -')
        print('O que voce gostaria de pesquisar?')
        print('Digite 0 para voltar.')
        print('Digite 1 para pesquisar por restaurante')
        print('Digite 2 para pesquisar por comida')
        print('Digite 3 para mostrar as categorias')
        
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
        elif optionPesq is 0:
            break
        else:
            print('Entrada inválida. Tente novamente.')
            break

def autentica():
    userEmail = None
    userPass = None
    while 1:

        print('Entre com seu e-mail ou digite 0 para voltar:')
        userEmail = input('> ')
        if userEmail is '0':
            print('\n')
            break
        print('Entre com sua senha:')
        userPass = input('> ')

        print('\n')

        # if userEmail is '0':
        #     break
        # chama função que autentica

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

    option = None
    while 1:
        print('- - - - - - - - - - - -')
        print('M E N U   I N I C I A L')
        print('- - - - - - - - - - - -')
        print('Digite 0 para sair do iDOOM')
        print('Digite 1 para cadastrar-se')
        print('Digite 2 para entrar')
        print('Digite 3 para pesquisar')
        print('Digite 4 para consultar o histórico de pedidos')
        # print('Digite 4 para mostrar as categorias de produtos disponíveis')
        # print('Digite 5 para inserir um produto em um restaurante')
        # print('Digite 6 para procurar restaurantes com a comida passada')
        # print('Digite 7 para deletar um produto de um restaurante específico')
        # print('Digite 8 para mostrar um histórico dos preços médios das comidas de um restaurante específico')
        # print('Digite 9 para motrar a lista do produto mais vendido')

        try:
            option = int(input('> '))
        except:
            print('Entrada inválida.')
            print('A entrada deve ser um número!')
            print('Tente novamente.')
            continue

        print('\n')

        if option is 1:
            cadastro()
        elif option is 2:
            autentica()
        elif option is 3:
            pesquisar()
        elif option is 4:
            pass
        elif option is 0:
            break
        else:
            print('Entrada inválida. Tente novamente')
            continue

        


if __name__ == '__main__':
    mainCLI()
