def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma += i

    return soma


def test_soma1():
    soma_elementos([1,1,1,1,1,]) == 5

def test_soma2():
    soma_elementos([1,2,1,2,1,]) == 7

def test_soma3():
    soma_elementos([5,5,5]) == 15