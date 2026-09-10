# Declaração da Classe
class ContaBancaria:
    # Metodo Construtor 
    def __init__(self, id=int, nomeTitular=str, saldo=0): 
        # Atributos
        self.id = id
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo: R$ {self.saldo:.2f}')

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R$ {valor:.2f} realizado')

    def saque(self, valor):
        if valor > self.saldo:
            print(f'Saque Negado, saldo total {self.saldo} insuficiente')
        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado')


cliente1 = ContaBancaria(1, 'Gustavo Marcello', 32000)
cliente1.saque(35000)
cliente1.deposito(8000)
print(cliente1.__dict__)