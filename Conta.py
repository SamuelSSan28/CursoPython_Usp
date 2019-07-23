from Cliente import Cliente

class Conta:
    def __init__(self,num,cliente,saldo,limite):
        self.cliente = cliente
        self.num = num
        self.saldo = saldo
        self.limite = limite


    def sacar(self,valor):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
        elif valor <= self.limite:
            if self.saldo > 0:
                self.limite -= (valor - self.saldo)
                self.saldo -= valor
            else:
                self.limite -= (valor)

        else:
            print("Saque Invalido")


    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Deposito Invalido!!")


    def extrato(self):
        print("Cliente:", self.cliente.nome)
        print("Saldo:",self.saldo)
        print("Limite:",self.limite)
        print("---------------------------\n")