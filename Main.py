class Main:
    pass

print("testando o projeto")

from Cliente import Cliente

from conta import conta

c1= Cliente("João", "114444-2222")
conta=conta(c1.nome,6565,0)

print(conta.titular,"numero: ",conta.numero,"seu saldo: ",conta.saldo)

print(c1)
print(c1.nome,"e",c1.telefone)