"""
EXERCÍCIO D40 - Verificador de Média
Crie um programa que:
1. Peça ao usuário para digitar três notas
2. Calcule a média das notas
3. Exiba a média com 2 casas decimais
4. exiba se o aluno foi:
    - Aprovado (média >= 7)
    - Recuperação (5 <= média < 7)
    - Reprovado (média < 5)
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1+n2+n3) / 3

if media >=7:
    print(f'Sua média: {media:.2f} Aprovado')
elif media < 5:
    print(f'Sua média: {media:.2f} Reprovado')
else:
    print(f'Sua média: {media:.2f} Recuperação')