"""
# Video com os desafios:  CeV Python POO: Aula 09 https://www.youtube.com/watch?v=CTbdydT9nlQ&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=27

EXERCÍCIO D32 - Conta bancária
Crie um programa que:
1. Contenha a classe abstrata ContaBancaria contendo:
    - _id
    - _titular
    - __saldo
    - __hash
    - depositar(valor, chave) (deposita o valor na conta pedindo a senha)
    - sacar(valor, chave) (saca o valor na conta pedindo a senha)
    - saldo - property get (visualizar o saldo pedindo a senha)
    - titular - property get (altera o titular pedindo a senha)
    - validarSenha(chave)
    - pedirSenha() (automático quando ao estanciar o objeto sem passar o __hash)
        - ao digitar a senha, deverá aparecer **** em cada caracter digitado
"""