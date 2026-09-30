"""
# Video com os desafios:  CeV Python POO: Aula 12 https://www.youtube.com/watch?v=CTbdydT9nlQ&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=27

EXERCÍCIO D32 - Conta bancária
Crie um programa que:
1. Contenha a classe abstrata ContaBancaria contendo:
    - _id
    - _titular
    - __saldoInicial
    - __senha (criptografada)
    - depositar(valor, chave) (deposita o valor na conta pedindo a senha)
    - sacar(valor, chave) (saca o valor na conta pedindo a senha)
    - saldo - property get (visualizar o saldo pedindo a senha)
    - titular - property get (altera o titular pedindo a senha)
    - validarSenha(senha)
    - pedirSenha() (automático quando ao estanciar o objeto sem passar o __hash)
"""
from hashlib import sha256

class ContaBancaria():
    def __init__(self, id:int, titular:str, saldoInicial:float, senha:str = None):
        self._id = id
        self._titular = titular
        self.__saldo = saldoInicial
        if senha == None:
             senha = self.pedirSenha()
        self.__senha = sha256(senha.encode('utf-8')).hexdigest()

        print(f'Conta {self._id} criada com sucesso. Saldo: R$ {self.__saldo:.2f}')

    @property
    def saldo(self):
         return f'Saldo atual: R$ {self.__saldo:.2f}'

    @property
    def titular(self):
         return f'Titular: {self._titular}'

    def pedirSenha(self) -> str:
        while True:
            senha = str(input('Digite uma senha com mais de 6 caracteres: '))
            if len(senha) >= 6:
                break
            else:
                print('\033[31mNova senha Inválida!\033[m')
        return senha      

    def deposito(self, valor):
            self.__saldo += abs(valor)
            print(f'Depósito de R$ {valor:.2f} realizado')

    def saque(self, valor, senha=None):
        if senha == None:
            senha = self.pedirSenha()
            
        validador = self.validarSenha(senha)
        if validador:
            valor = abs(valor)
            if valor > self.__saldo:
                print(f'Saque Negado, saldo total {self.__saldo} insuficiente')
            else:
                self.__saldo -= valor
                print(f'Saque de R$ {valor:.2f} realizado')
        

    def validarSenha(self, senha) -> bool:
        hashSenha = sha256(senha.encode('utf-8')).hexdigest()
        if hashSenha == self.__senha:
            return True
        else:
            print('\033[31mSenha Inválida!\033[m')
            return False


cliente1 = ContaBancaria(1, 'Gustavo Marcello', 32000, '@MinhaSenha1')
cliente1.saque(3000)
cliente1.deposito(8000)
print(cliente1.saldo)