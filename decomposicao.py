def ehPrimo(n):
    i = 2
    while i < n:
        if  n%i == 0:
            return False
        i += 1

    return True



def decompoe(n):
    fator = 2
    resp = ""
    while fator <= n :
        multiplicidade  = 0
        if ehPrimo(fator):
            while n%fator == 0:
                n = n//fator
                multiplicidade += 1
            if multiplicidade > 0:
                print("Fator:",fator, " multiplicadade:",multiplicidade)
        fator += 1

    return resp



print(decompoe(1000))