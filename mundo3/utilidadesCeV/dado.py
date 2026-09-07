def valorInvalidoMsg():
    return f'\033[0;33mERRO: valor inválido \033[m'


def leiaDinheiro(msg):
    valido= False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(valorInvalidoMsg())
        else:
            valido = True
            return float(entrada)
        

def leiaInt():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))

            print(f'Validado número inteiro: {num}')
            break
        except:
            print(valorInvalidoMsg())

def leiaFloat():
    while True:
        try:
            num = float(input('Digite um número flutuante: '))

            print(f'Validado número flutuante: {num}')
            break
        except:
            print(valorInvalidoMsg())