def maior_primo(n):
    while n > 2:
        cont = 0
        for j in range(2,n):
            if n%j == 0:
               cont += 1

        if cont == 0:
            return n

        n -= 1

    return n


def test_maximo1():
    assert  maior_primo(2) == 2

def test_maximo2():
    assert  maior_primo(4) == 3

def test_maximo3():
    assert  maior_primo(6) == 5

def test_maximo4():
    assert  maior_primo(100) == 97

