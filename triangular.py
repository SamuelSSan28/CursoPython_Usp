x = int(input("Insira X "))

n = 1
m = 1

while m < x:
    m = n * (n+1) *(n+2)
    n = n+1


if m == x:
    print("triangular")
else:
    print("nao é")