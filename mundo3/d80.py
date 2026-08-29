"""
EXERCÍCIO D80 - Lista ordenada sem repetições
Crie um programa que:
1. Leia vários números inteiros pelo teclado
2. Adicione-os a uma lista, sem repetições
3. Exiba a lista ordenada
4. Pergunte ao usuário se ele deseja continuar [S/N]

Obs*: Não utilize o método sort() para ordenar a lista, faça isso manualmente.
"""

valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        for i, v in enumerate(valores):
            if n < v:
                valores.insert(i, n)
                break
        else:
            valores.append(n)

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        break

print(valores)
