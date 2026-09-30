class Mae():
    def __init__(self, nome:str = 'Mãe'):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz pudim de pão com calda')

    def fritar_coxinha(self):
        print(f'{self.nome} frita coxinha com óleo de soja')


class Filha(Mae):
    def __init__(self, nome = 'Filha'):
        super().__init__(nome)

    def fazer_pudim(self):
        print(f'{self.nome} faz pudim de chocolate com granulado')

class Filho(Mae):
    def __init__(self, nome = 'Filho'):
        super().__init__(nome)

    def fritar_coxinha(self):
        print(f'{self.nome} frita coxinha na air fryer')


mae = Mae('Eliana')
filho = Filho('Gustavo')
filha = Filha('Stela')

mae.fazer_pudim()
mae.fritar_coxinha()

filha.fazer_pudim()
filha.fritar_coxinha()

filho.fazer_pudim()
filho.fritar_coxinha()