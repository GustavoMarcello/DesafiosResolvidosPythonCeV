def msgColorido(msg=str, codCor=int):
    """
    código de cores:
     branco - 30
     vermelho - 31
     verde - 32
     amarelo - 33
     azul - 34
     roxo - 35
     ciano - 36
     cinza - 37
    """
    return f'\033[{codCor}m{msg}\033[m'


def menu(opcoes=list, tamanho=int, cor=int):
    print(msgColorido('-', cor)*tamanho)
    print(msgColorido('MENU PRINCIPAL', cor).center(tamanho))
    print(msgColorido('-', cor)*tamanho)
    for i , opcao in enumerate (opcoes):
        print(f'\033[33m{i+1}\033[m - \033[34m{opcao}\033[m')
    print(msgColorido('-', cor)*tamanho)


def titulo(titulo=str, tamanho=int, cor=int):
    print(msgColorido('-', cor)*tamanho)
    print(msgColorido(titulo, cor).center(tamanho))
    print(msgColorido('-', cor)*tamanho)


def verificaTXT(nomeTXT=str):
    try:
        a = open(nomeTXT, 'rt')
        a.close()
    except:
        a = open(nomeTXT, 'wt+')
        a.close()


def lerTXT(nomeTXT=str):
    try:
        a = open(nomeTXT, 'rt')
        for linha in a:
            dado = linha.split(';')
            dado[1]= dado[1].replace('\n', ' anos')
            print(msgColorido(f'{dado[0]:<25} {dado[1]:>24}', 33))
        a.close()
    except:
        print('Erro ao ler o arquivo')


def cadastrarTXT(nomePessoa=str, idadePessoa=str, nomeTXT=str):
    try:
        a = open(nomeTXT, 'at')
        a.write(f'{nomePessoa};{idadePessoa}\n')
        a.close()
    except:
        print('Erro ao abrir o arquivo')


def validarNome(mensagem=str):
    while True:
        nome = str(input(mensagem)).strip()
        if nome and all(caractere.isalpha() or caractere.isspace() for caractere in nome):
            return nome
        print(msgColorido('ATENÇÃO Nome inválido. Digite apenas letras e espaços.', 31))


def validarIdade(mensagem=str):
    while True:
        try:
            idade = int(input(mensagem).strip())
            if idade >= 0:
                return idade
        except ValueError:
            pass
        print(msgColorido('ATENÇÃO Idade inválida. Digite um número inteiro não negativo.', 31))
