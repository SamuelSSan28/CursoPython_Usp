def remove_repetidos(lista):
    i = 0
    while i  < (len(lista)):
       # print(len(lista))
        if lista.count(lista[i]) > 1:
            del lista[i]
            i -= 1
        i += 1
    return sorted(lista)


def test_remove_repetidos1():
    assert remove_repetidos([1,2,1,3,4,5,8,4,5]) == [2, 1, 3, 8, 4, 5]

def test_remove_repetidos2():
    assert remove_repetidos([1,2,2,1,3,4,5,8,4,5]) == [2, 1, 3, 8, 4, 5]

def test_remove_repetidos3():
    assert remove_repetidos([1,2,2,1,3,4,5,8,4,8,3,5]) == [2, 1, 4, 8, 3, 5]


print(remove_repetidos([1,2,1,3,4,5,8,4,5]))