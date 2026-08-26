"""
EXERCÍCIO D49 - Gerador de Tabuada Personalizada
Crie um programa que:
1. Peça ao usuário para digitar um número
2. Peça o intervalo: número inicial e final da multiplicação
3. Gere a tabuada nesse intervalo
4. Exiba cada multiplicação com seu resultado
"""

num = int(input('Digite um número: '))
inicio = int(input('Digite o valor inicial  do multiplicador: '))
final = int(input('Digite o valor final  do multiplicador: '))

for i in range(inicio, final):
    print(f' {num} X {i} = {num*i}')