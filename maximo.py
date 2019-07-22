def maximo(x,y):
    if x >= y :
        return x
    else:
        return y

def test_maximo1():
    assert maximo(1,2) == 2

def test_maximo2():
    assert maximo(4, 2) == 4

def test_maximo3():
    assert maximo(3,5) != 3

def test_maximo4():
    assert maximo(7,10) == 10

