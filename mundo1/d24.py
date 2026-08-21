"""
EXERCÍCIO D24 - Verificador de Nomes que Começam com 'SANTO'
Crie um programa que:
1. Peça ao usuário para digitar o nome de uma cidade
2. Converta para maiúsculas
3. Verifique se os primeiros 5 caracteres são 'SANTO'
4. Exiba True ou False
"""

cidade = str(input('Digite o nome de uma cidade: '))
upperCidade = cidade.upper()
splitCidade = upperCidade.split()

print(f'Nome da cidade digitado: {upperCidade}')
print(f'Cidade digitada começa com "SANTO"? {'SANTO' in splitCidade[0]}')