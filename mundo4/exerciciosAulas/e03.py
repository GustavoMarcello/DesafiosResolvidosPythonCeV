# Declaração da Classe
class ContaBancaria:
    # Metodo Construtor 
    def __init__(self, id=int, nomeTitular=str, saldo=0): 
        # Atributos
        self.id = id
        self.nomeTitular = nomeTitular
        self.__saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo: R$ {self.__saldo:.2f}')

    def deposito(self, valor):
        self.__saldo += abs(valor)
        print(f'Depósito de R$ {valor:.2f} realizado')

    def saque(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'Saque Negado, saldo total {self.__saldo} insuficiente')
        else:
            self.__saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado')


cliente1 = ContaBancaria(1, 'Gustavo Marcello', 32000)
cliente1.saque(3000)
cliente1.deposito(8000)
print(cliente1.nomeTitular)