import math


x1 = int(input("Insira X1 "))
y1 = int(input("Insira Y1: "))
x2 = int(input("Insira X2: "))
y2 = int(input("Insira Y2: "))


d = (x1 - x2)**2 + (y1 - y2)**2
d = math.sqrt(d)

if d >= 10:
    print("longe")
else:
    print("perto")
