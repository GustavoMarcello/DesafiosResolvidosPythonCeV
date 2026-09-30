"""
# Video com os desafios:  CeV Python POO: Aula 12 https://www.youtube.com/watch?v=CTbdydT9nlQ&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=27

EXERCÍCIO D30 - gerenciador de senhas hash SHA-256
Crie um programa que:
1. Contenha a classe abstrata Credencial contendo:
    - senha
    - __hash
    - validarSenha(senha)
    - alterarSenha(novaSenha)
"""
from hashlib import sha256

class Credencial():
    def __init__(self, senha:str = '@MinhaSenha1'):
        self.__hash = sha256(senha.encode('utf-8')).hexdigest()

    @property
    def senha(self):
        return self.__hash

    def validarSenha(self, senha):
        hashSenha = sha256(senha.encode('utf-8')).hexdigest()
        if hashSenha == self.__hash:
            print('\033[32mSenha Validada!\033[m')
        else:
            print('\033[31mAs senhas não conferem!\033[m')

    def alterarSenha(self, novaSenha=str):
        if len(novaSenha) > 3:
            self.__hash = sha256(novaSenha.encode('utf-8')).hexdigest()
            print('\033[32mSenha Alterada com Sucesso!\033[m')
        else:
            print('\033[31mNova senha Inválida!\033[m')


credencial = Credencial()
credencial.alterarSenha('NovaSenha$2')
credencial.validarSenha('NovaSenha$2')
