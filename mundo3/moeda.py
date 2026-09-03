
def aumentar(preco, valor, formatar=False):
    conta = preco + valor
    if formatar:
        conta = moeda(conta)
    return conta

def diminuir(preco, valor, formatar=False):
    conta = preco - valor
    if formatar:
        conta = moeda(conta)
    return conta

def dobro(preco, formatar=False):
    conta = preco * 2
    if formatar:
        conta = moeda(conta)
    return conta

def metade(preco, formatar=False):
    conta = preco / 2
    if formatar:
        conta = moeda(conta)
    return conta

def moeda(preco=float):
    return f'R$ {preco:.2f}'

def resumo(preco, valor):
    print(f'O valor de {preco} + {valor} = {aumentar(preco, valor, True)}')
    print(f'O valor de {preco} - {valor} = {diminuir(preco, valor, True)}')
    print(f'O dobro de {preco} = {dobro(preco, True)}')
    print(f'A medade de {preco} = {metade(preco, True)}')