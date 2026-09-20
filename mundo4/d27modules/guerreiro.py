from .personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome=str, vida=int, golpes=list):
        super().__init__(nome, vida, golpes)

    def ataqueComArma(self, inimigo):
        rolagemD12 = self.rolarD12()
        dano = 2 + rolagemD12
        print(f'Dano araque com arma: {dano}')
        vidaRestante = inimigo.receberDano(dano)

        print(f'Vida restante {inimigo.nome}: {vidaRestante}')

    def arremecarAdagas(self, inimigo):
        danoBase = 3
        dano = danoBase

        for i in range(1, 3):
            d6 = self.rolarD6()
            print(f'Adaga {i}: {d6}')
            dano += d6

        print(f'Dano base: {danoBase}')
        print(f'Dano total: {dano}')
        vidaRestante = inimigo.receberDano(dano)

        print(f'Vida restante {inimigo.nome}: {vidaRestante}')