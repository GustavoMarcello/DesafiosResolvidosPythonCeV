"""
EXERCÍCIO D115 - Sistema de cadastro modularizado
Crie um programa que:
1. Permita cadastrar nome e idade de pessoas
2. Guarde essas informações em um arquivo de texto
    - Crie o arquivo de texto automaticamente caso não exista
3. O sistema deverá ter duas opções iniciais:
    - Cadastrar pessoas
    - Listar pessoas cadastradas
    - Sair
"""

from utilidadesCeV.utilsD115 import verificaTXT, menu, titulo, cadastrarTXT, msgColorido, lerTXT, validarNome, validarIdade
from time import sleep

txt = 'texto/arquivoCeV.txt'
verificaTXT(txt)

tamanho = 50
opcoes = ['Cadastrar pessoa', 'Listar cadastros', 'Sair']

while True:
    menu(opcoes, tamanho, 34)
    opcao = str(input('Digite uma opção: ')).strip()

    match opcao:
        case '1':
            titulo('NOVO CADASTRO', tamanho, 32)
            nome = validarNome(msgColorido('Digite o nome da pessoa: ', 32))
            idade = validarIdade(msgColorido('Digite a idade da pessoa: ', 32))
            cadastrarTXT(nome, idade, txt)
            print(msgColorido('-'*tamanho, 32))
        case '2':
            titulo('PESSOAS CADASTRADAS',tamanho, 33)
            lerTXT(txt)
            print(msgColorido('-'*tamanho, 33))
            sleep(2)
        case '3':
            titulo('Obrigado, até a próxima!', tamanho, 36)
            sleep(1)
            break
        case _:
            print(msgColorido('ATENÇÃO: Digite uma opção válida', 31))
            sleep(1)
    sleep(1)