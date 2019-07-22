nome = input("Digite o nome do cliente: ")
data = input("Digite o dia de vencimento: ")
mes = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")


if valor.count(",")== 0:
    print("Olá, {}\nA sua fatura com vencimento em {} de {} no valor de R$ {},00 está fechada.".format(nome,data,mes,valor))
else:
    print("Olá, {}\nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.".format(nome,data,mes,valor))
