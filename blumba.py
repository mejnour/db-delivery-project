def funcaoTeste(param1 = None, param2 = None):
    if param1 is not None and param2 is not None:
        print('Usei param 1 e param2')
    elif param2 is not None:
        print('Usei só param2')
    elif param1 is not None:
        print('Usei só param1')

if __name__ == "__main__":
    p1 = p2 = 0

    funcaoTeste(p1, None)
    funcaoTeste(None, p2)
    funcaoTeste(p1, p2)