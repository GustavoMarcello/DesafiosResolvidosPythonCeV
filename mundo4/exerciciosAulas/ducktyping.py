class Porta():
    def abrir(self):
        print(f'Gire a Maçaneta e puxe a porta')

class Empresa():
    def abrir(self):
        print(f'Traga seus documentos para a contabilidade')

class Ovo():
    def abrir(self):
        print(f'Quebre a casca e despeje em um recipiente a gema com a clara')

class Pedra():
    pass


# DUCKTYPING
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f'\033[31mErro ao tentar abrir: {objeto.__class__.__name__}\033[m')


a = Porta()
b = Empresa()
c = Ovo()
d = Pedra()

tentar_abrir(a)
tentar_abrir(b)
tentar_abrir(c)
tentar_abrir(d)