from .personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome=str, vida=int, golpes=list):
        super().__init__(nome, vida, golpes)

    def fireball(self, inimigo):
        rolagemD12 = self.rolarD12()
        dano = 6 + rolagemD12
        print(f'Dano fireball: {dano}')
        vidaRestante = inimigo.receberDano(dano)
        print(f'Vida restante {inimigo.nome}: {vidaRestante}')

    def magicMissles(self, inimigo):
        dano = 0

        for i in range(1, 4):
            d6 = self.rolarD6()
            print(f'Missle {i}: {d6}')
            dano += d6

        print(f'Dano total: {dano}')

        vidaRestante = inimigo.receberDano(dano)
        print(f'Vida restante {inimigo.nome}: {vidaRestante}')