class Numero():
    def __init__(self, num:int|float):
        self._num = num
        
    def dobrar(self):
        self._num = self._num * 2

    def __str__(self):
        return f'Valor de número: {self._num}'


class Texto():
    def __init__(self, txt:str):
            self._txt = txt
    
    def dobrar(self):
        self._txt = self._txt + " " + self._txt

    def __str__(self):
        return f'O texto é: {self._txt}'


class Lista():
    def __init__(self, lista:list):
            self._lista = lista
    
    def dobrar(self):
        self._lista = self._lista + self._lista

    def __str__(self):
        return f'Ítens da lista: {self._lista}'


class Papel():
    def __init__(self):
            self.__dobrado = False
    
    def dobrar(self):
        self.__dobrado = True

    def __str__(self):
        return f'O papel está dobrado? {self.__dobrado}'

class Casa():
    def __init__(self):
        pass

    def __str__(self):
        return f'Era uma casa muito engraçada'


# DUCKTYPING
def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except Exception as erro:
         print(f'\033[31mErro ao tentar dobrar: {objeto.__class__.__name__}\033[m')
         print(f'\033[31m{erro}\033[m')

a = Numero(123)
b = Texto('Python')
c = Lista(['Python', True, 1.5])
d = Papel()
e = Casa()

tente_dobrar(a)
tente_dobrar(b)
tente_dobrar(c)
tente_dobrar(d)
tente_dobrar(e)

print(a)
print(b)
print(c)
print(d)
print(e)