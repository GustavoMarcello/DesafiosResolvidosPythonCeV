"""
EXERCÍCIO D114 - Verificando site disponível
Crie um programa que:
1. Contenha uma função que receba como parâmetro o endereço de um site
2. Retorne se o site está acessível ou não
"""

from urllib import request

url = 'https://www.pudim.com.br'

try:
    cabecalho = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'
    }

    requisicao = request.Request(url, headers=cabecalho)
    request.urlopen(requisicao)

    print('Url acessada')

except Exception as erro:
    print(f'Url não acessível: {erro}')
