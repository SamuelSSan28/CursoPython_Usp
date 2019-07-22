def fat(n):
    if  n <= 1:
        return 1
    return n*fat(n-1)

x = int(input("Informe um número: "))

while x > 0:
    print(fat(x))
    x = int(input("Informe um número: "))


