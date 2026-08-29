"""EXERCÍCIO D83 - Validando expressões matemáticas
Crie um programa que:
1. Leia uma expressão matemática pelo teclado
2. Verifique se a expressão está com os parênteses abertos e fechados na ordem correta
3. Exiba se a expressão é válida ou não
"""

expressao = input('Digite uma expressão: ')

pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)

    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')