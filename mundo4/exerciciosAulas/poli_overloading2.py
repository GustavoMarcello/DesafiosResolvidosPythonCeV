# Operators:
#   c1 == c2      c1.__eq__(c2)
#   c1 != c2      c1.__ne__(c2)
#   c1  < c2      c1.__lt__(c2)
#   c1 <= c2      c1.__le__(c2)
#   c1  > c2      c1.__gt__(c2)
#   c1 >= c2      c1.__ge__(c2)
#   c1 += c2      c1.__iadd__(c2)
#   c1 -= c2      c1.__isub__(c2)

class Carteira():
    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return (f'Seu saldo é de {self.saldo:.2f} reais')

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        return False

    def __iadd__(self, valor: int|float):
        self.__saldo += valor
        return self

    def __isub__(self, valor: int|float):
        self.__saldo -= valor
        return self
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('\033[31mVocê não tem autorização para alterar o saldo dessa forma\033[m')


carteira1 = Carteira(1500)
carteira2 = Carteira(1000)

carteira2 += 500
print(carteira1 == carteira2)