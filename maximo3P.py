def maximo(x,y,z):
    if x >= y :
        if x >= z:
            return x
        else:
            return z
    else:
        if y >= z:
            return y
        else:
            return z


def test_maximo1():
    assert maximo(1,2,0) == 2

def test_maximo2():
    assert maximo(3,4, 2) == 4

def test_maximo4():
    assert maximo(5,7,10) == 10

