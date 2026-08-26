"""
EXERCÍCIO D47 - Contador de Números Pares
Crie um programa que:
1. Conte todos os números pares de 1 até 50
2. Exiba cada número par encontrado
3. Ao final, exiba a quantidade total de números pares encontrados
"""
count = 0
for i in range(2, 50, 2):
    count += 1
print(f'Existem {count} números pares entre 1 e 50')

