"""
EXERCÍCIO D10 - Conversão de Moeda (Reais para Dólar)
Crie um programa que:
1. Peça ao usuário para digitar um valor em reais (R$)
2. Converta para dólar usando a taxa de câmbio de 1 dólar = 5.2 reais
3. Exiba o valor em reais e em dólar com 2 casas decimais
"""
cotacao = 5.2

reais = float(input('Digite um valor em reais: '))
conversao = reais / cotacao
print(f'R${reais:.4f} = ${conversao:.4f}')