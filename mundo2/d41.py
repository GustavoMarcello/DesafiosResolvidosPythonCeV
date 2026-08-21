"""
EXERCÍCIO D41 - Classificador de Atletas
Crie um programa que:
1. Peça ao usuário para digitar a idade de um atleta
2. Classifique o atleta em uma das categorias:
   - Até 9 anos: MIRIM
   - Até 14 anos: INFANTIL
   - Até 19 anos: JÚNIOR
   - Até 25 anos: SÊNIOR
   - Acima de 25 anos: MASTER
"""

idade = int(input('Digite a idade do atleta: '))

if idade <= 9:
    print('Até 9 anos: MIRIM')
elif idade <=14:
    print('Até 14 anos: INFANTIL')
elif idade <=19:
    print('Até 19 anos: JÚNIOR')
elif idade <=25:
    print('Até 25 anos: SÊNIOR')
else:
    print('Acima de 25 anos: MASTER')