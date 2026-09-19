from .personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome=str, vida=int, golpes=list):
        super().__init__(nome, vida, golpes)

    def ataqueComArma(self):
        rolagemD12 = self.rolarD12()
        dano = 2 + rolagemD12
        vidaRestante = self.receberDano(dano)
        return vidaRestante

    def arremecarAdagas(self):
        dano = 3

        for i in range(1, 3):
            d6 = self.rolarD6()
            print(f'Dado {i}: {d6}\n')
            dano += d6

        vidaRestante = self.receberDano(dano)
        return vidaRestante