from .personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome=str, vida=int, golpes=list):
        super().__init__(nome, vida, golpes)

    def fireball(self):
        rolagemD12 = self.rolarD12()
        dano = 6 + rolagemD12
        vidaRestante = self.receberDano(dano)
        return vidaRestante

    def magicMissles(self):
        dano = 0

        for i in range(1, 4):
            d6 = self.rolarD6()
            print(f'Dado {i}: {d6}\n')
            dano += d6

        vidaRestante = self.receberDano(dano)
        return vidaRestante