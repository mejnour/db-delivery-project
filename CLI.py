import curses
import functions as fn
from curses import wrapper

def cadastro():
    sel = None
    
    print('\n')
    print('Bem-vindo ao cadastro.')

    while 1:
        print('Digite 1 para cadastrar um usuário')
        print('Digite 2 para cadastrar um restaurante')

        sel = int(input())

        if sel is 1:
            print('Por favor, informe o usuário:')
            userLogin = input()
            print('Por favor, informe a senha:')
            userPass = input()

            print('. . . . .')

            fn.askUserInput()
            break
        if sel is 2:
            print('Por favor, informe o nome do Restaurante:')
            restaurantLogin = input()
            print('Por favor, informe a senha:')
            restaurantPass = input()

            print('. . . . .')

            fn.askRestaurantInput()
            break
        else:
            print('Opção inválida. Tente novamente.')
            continue

def mainCLI():
    while 1:
        print('\nDigite 0 para TRALALA dos testes')
        print('Digite 99 para cadastrar-se')
        print('Digite 1 para inserir Usuário')
        print('Digite 2 para inserir Restaurante')
        print('Digite 3 para mostrar comidas de um Restaurante')
        print('Digite 4 para mostrar as categorias de produtos disponíveis')
        print('Digite 5 para inserir um produto em um restaurante')
        print('Digite 6 para procurar restaurantes com a comida passada')
        print('Digite 7 para deletar um produto de um restaurante específico')
        print('Digite 8 para mostrar um histórico dos preços médios das comidas de um restaurante específico')
        print('Digite 9 para motrar a lista do produto mais vendido')

        sel = int(input())

        if sel is 99:
            cadastro()


if __name__ == '__main__':
    mainCLI()
    