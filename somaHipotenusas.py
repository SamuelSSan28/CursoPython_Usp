import  math

def eh_Hipotenusa(n):
    i = j = 1
    while i < n:
        while j < n:
            hipo = i**2 + j**2
            if hipo == n**2:
                return True
            j+=1
        i +=1
        j = 1

    return False


def soma_hipotenusas(n):
    i = 1
    soma = 0
    while i <= n:
        if eh_Hipotenusa(i):
            soma += i
        i += 1

    return soma
