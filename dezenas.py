x = input("Digite um número inteiro: ")

if len(x) > 1:
    print("O dígito das dezenas é {}".format(x[len(x) - 2]))
else:
    print("O dígito das dezenas é 0")

