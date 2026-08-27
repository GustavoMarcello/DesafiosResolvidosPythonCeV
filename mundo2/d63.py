"""
EXERCÍCIO D63 - Gerador de Sequência de Fibonacci
Crie um programa que:
1. Peça ao usuário para digitar quantos termos da sequência de Fibonacci deseja
2. Gere a sequência onde cada número é a soma dos dois anteriores (começando com 0 e 1)
3. Exiba toda a sequência
"""

termos = int(input('Digite quantos termos da Sequencia de Fibonacci você deseja visualizar: '))

#Valores iniciáis da sequencia de fibonacci
t1 = 0
t2 = 1
resultadoSequencia = '0, 1'

count = 3
while count <= termos:
    t3 = t1 + t2
    t2 = t3
    t1 = t2
    resultadoSequencia += f', {t3}'
    count += 1

print(resultadoSequencia)
