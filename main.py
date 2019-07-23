from Cliente import Cliente
from Conta import Conta

cliente1 = Cliente("Samuel","061225889",19)
cliente2 = Cliente("João","439225889",45)
cliente3 = Cliente("Carlos","014225889",58)


conta1 = Conta(123,cliente1,0.0,500)
conta2 = Conta(321,cliente2,400.0,1000)
conta3 = Conta(159,cliente3,800.0,2500)

conta1.depositar(5)
conta1.extrato()


conta2.sacar(250)
conta2.extrato()

conta3.depositar(100)
conta3.extrato()
conta3.sacar(150)
conta3.extrato()


conta1.sacar(500)
conta1.extrato()
conta1.sacar(5)
conta1.extrato()