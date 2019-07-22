import math

def delta(a,b,c):
    return b**2 - (4*a*c)

def bhaskara(a,b,c):
    d = delta(a,b,c)
    if d < 0:
        print("esta equação não possui raízes reais")
    elif d == 0:
        raiz = (-1 * b + math.sqrt(d)) / (2 * a)
        print("a raiz desta equação é", raiz)
    else:
        raiz1 = (-1 * b + math.sqrt(d)) / (2 * a)
        raiz2 = (-1 * b - math.sqrt(d)) / (2 * a)
        print("as raízes da equação são", min(raiz1, raiz2), "e", max(raiz2, raiz1))

def main():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    bhaskara(a,b,c)


main()




