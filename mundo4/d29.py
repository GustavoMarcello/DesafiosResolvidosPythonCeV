"""
# Video com os desafios:  CeV Python POO: Aula 12 https://www.youtube.com/watch?v=CTbdydT9nlQ&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=27

EXERCÍCIO D29 - Diário
Crie um programa que:
1. Contenha a classe Diário contendo:
    - __segredos[]
    - __senha
    - ler() - retorna os segredos se a senha estiver correta
    - escrever(mensagem) - escreve a mensagem se a senha estiver correta
"""

class Diario():
    def __init__(self, senha:str = 'Minha Senha'):
        self.__senha = senha
        self.__segredos = []

    @property
    def senha(self):
        raise PermissionError(f'Sem permissão para acessar propriedade senha')

    def escrever(self, mensagem):
        self.__segredos.append(mensagem)
        print('\033[30mMensagem escrita com sucesso no diário\033[m')


    def ler(self):
        senha = ''
        while senha != self.__senha:
            senha = str(input('Digite a senha do diário: '))
            if senha == self.__senha:
                print('Segredos do diário:')
                for i in self.__segredos:
                    print(f'\033[34m - {i}\033[m')
            else:
                print('\033[31mSenha incorreta!\033[m')


diario = Diario()
diario.escrever('Feito é melhor que perfeito.')
diario.escrever('Você é mais forte do que imagina.')
diario.escrever('O melhor está por vir.')

diario.ler()