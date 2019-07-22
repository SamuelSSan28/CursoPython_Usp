l = int(input("Digite o lado do Retangulo: "))
h = int(input("Digite a altura do Retangulo: "))

i = 0

while i < h:
    j = 0
    while j < l:
        if j > 0 and j < l-1 and i>0 and i < h-1:
            print(end=" ")
        else:
            print("#",end = "")
        j += 1
    print("")
    i += 1