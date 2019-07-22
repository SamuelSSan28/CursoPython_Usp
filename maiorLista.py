def maior_elemento(lista):
    return max(lista)


def test_maior():
    assert maior_elemento([1,2,3,4,5])  == 5

def test_maior2():
    assert maior_elemento([1,2,10,4,5])  == 10