def ehPrimo(n):
    i = 2
    while i < n:
        if  n%i == 0:
            return False
        i += 1

    return True

def n_primos(n):
    cont = 0
    i = 2
    while i <= n:
        if ehPrimo(i):
            cont += 1
        i += 1

    return cont


def test_1():
    assert  n_primos(2) == 1

def test_2():
    assert  n_primos(4) == 2

def test_3():
    assert  n_primos(5) == 3

def test_4():
    assert  n_primos(121) == 30