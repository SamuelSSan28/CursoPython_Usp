def vogal(letra):
    vogais = ["a","e","i","o","u","A","E","I","O","U"]

    if letra in vogais:
        return True
    else:
        return False


def test_vogal1():
    assert vogal("a") == True

def test_vogal2():
    assert vogal("b") == False

def test_vogal3():
    assert vogal("E") == True

def test_vogal4():
    assert vogal("z") == False