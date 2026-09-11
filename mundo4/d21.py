"""
EXERCÍCIO D21 - Classe Caneta
Crie um programa que:
1. Contenha a classe Caneta contendo atributo:
    - cor
2. Crie o método escrever() que:
    - Escreva um texto passado pelo usuário
    - O texto deverá estar na cor escolhida pelo usuário
*Cod das cores:
    \033[31mVermelho\033[m
    \033[32mVerde\033[m
    \033[33mAmarelo\033[m
    \033[34mAzul\033[m
    \033[35mRoxo\033[m
    \033[36mCiano\033[m
    \033[37mBranco\033[m
"""

class Caneta:
    def __init__(self, cor=str):
        self.cor = cor.strip().upper()

    def escrever(self,msg=str):
        
        codCor = {
            'VERMELHO': 31,
            'VERDE': 32,
            'AMARELO': 33,
            'AZUL': 34,
            'ROXO': 35,
            'CIANO': 36,
            'BRANCO': 37
        }

        if not self.cor in codCor:
            print('ERRO: Cor incorreta ou indisponível')
        else:
            print(f'\033[{codCor[self.cor]}m{msg}\033[m')


canetaAmarela = Caneta('amarelo')
canetaAmarela.escrever('Olá Mundo!')
canetaAzul = Caneta('azul')
canetaAzul.escrever('Olá Mundo!')
canetaRoxa = Caneta('roxo')
canetaRoxa.escrever('Olá Mundo!')