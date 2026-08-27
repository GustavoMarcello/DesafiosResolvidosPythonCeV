"""
EXERCÍCIO D59 (Melhorado) - Calculadora Completa
Crie um programa que:
1. Mostre um menu de opções:
    - [1] Somar
    - [2] Subtrair
    - [3] Multiplicar
    - [4] Dividir
    - [5] Sair/Encerrar
2. Entre as opções 1 à 4, solicite dois números e realize a operação demonstrando o resultado
3. Retorne ao Menu em seguida a operação
4. Encerre o programa ao inserir opção 5
"""

opcaoMenu = 0

while opcaoMenu != 5:
    opcaoMenu = int(input(
'''
Digite uma opção:
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir
    [5] Sair/Encerrar
'''
                    ))
    if opcaoMenu != 5:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))

        if opcaoMenu == 1:
            resultado = n1 + n2
        elif opcaoMenu == 2:
            resultado = n1 - n2
        elif opcaoMenu == 3:
            resultado = n1 * n2
        else:
            resultado = n1 / n2

        print(f'Resultado: {resultado}')
    else:
        print('Fim')