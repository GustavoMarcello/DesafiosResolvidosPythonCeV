"""
EXERCÍCIO D32 - Verificador de Ano Bissexto
Crie um programa que:
1. Peça ao usuário para digitar um ano
2. Verifique se é bissexto aplicando as regras:
   - É divisível por 400? Então é bissexto
   - É divisível por 100? Então NÃO é bissexto
   - É divisível por 4? Então é bissexto
   - Caso contrário: NÃO é bissexto
3. Exiba se o ano é bissexto ou não
"""

ano = int(input('Digite um ano: '))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print(f'{ano} é bissexto!')
else:    
    print(f'{ano} NÃO é bissexto!')