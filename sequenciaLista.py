numeros = []
while True:
    n = int(input("Digite o número: "))
    if n == 0:
        break
    else:
        numeros.append(n)

for i in numeros[::-1]:
    print(i)

print("%d teste" %(1))