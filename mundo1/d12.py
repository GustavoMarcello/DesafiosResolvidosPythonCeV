"""
EXERCÍCIO D12 - Desconto de 5% em Produto
Crie um programa que:
1. Peça ao usuário para digitar o preço de um produto
2. Calcule o preço com desconto de 5%
3. Exiba o preço original e o preço com desconto em reais
"""

preco = float(input('Digite o valor em reais do produto: '))
print(f'5% de desconto para R${preco:.2f}: R${(preco*0.95):.2f}')