from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str):
        self.nome = nome

    @abstractmethod
    def emitirSom(self):
        pass


class Pato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitirSom(self):
        print(f'{self.nome} é {self.__class__.__name__} e fez Quack Quack')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitirSom(self):
        print(f'{self.nome} é {self.__class__.__name__} fez AU AU AU')


class Poodle(Cachorro):
    def __init__(self, nome):
        super().__init__(nome)

    # Note que não tem emitir som 
    # sendo puxado da classe mãe


class Pitbull(Cachorro):
    def __init__(self, nome):
        super().__init__(nome)

    def emitirSom(self):
        print(f'{self.nome} é {self.__class__.__name__} fez RUFF RUFF')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitirSom(self):
        print(f'{self.nome} é {self.__class__.__name__} e fez MIAAAWWW')


class Galinha(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitirSom(self):
        print(f'{self.nome} é {self.__class__.__name__} e fez Pó Pó Pó')
        

pato = Pato('Donald')
cachorro = Cachorro('Snoop')
poodle = Poodle('Pipoca')
pitbull = Pitbull('Athus')
gato = Gato('Frajola')
galinha = Galinha('Fifi')

pato.emitirSom()
cachorro.emitirSom()
poodle.emitirSom()
pitbull.emitirSom()
gato.emitirSom()
galinha.emitirSom()