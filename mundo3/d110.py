"""
EXERCÍCIO D110 - Reduzindo código com funções
1. Crie a função resumo() dentro do módulo moeda.py,
2. Mostre algumas informações geradas pelas funções que já temos no módulo moeda.py
""" 
import moeda

valor = 12

preco = float(input('Digite um preço: '))
moeda.resumo(preco, valor)