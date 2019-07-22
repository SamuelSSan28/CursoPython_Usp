import math
a = float(input("Insira A: "))
b = float(input("Insira B: "))
c = float(input("Insira C: "))

delta = b * b - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é", raiz)
else:
    raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)
    print("as raízes da equação são", min(raiz1,raiz2),"e", max(raiz2,raiz1))