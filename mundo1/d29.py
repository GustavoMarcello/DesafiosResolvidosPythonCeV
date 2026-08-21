"""
EXERCÍCIO D29 - Cálculo de Multa por Excesso de Velocidade
Crie um programa que:
1. Peça ao usuário para digitar a velocidade do carro
2. Se a velocidade for maior que 80 km/h:
   - Exiba "Você foi multado!"
   - Calcule a multa: (velocidade - 80) * 7
   - Exiba o valor da multa
3. Se for igual ou menor que 80 km/h:
   - Exiba "Tenha um bom dia! Dirija com segurança!"
"""

velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em {multa} reais')
else:
    print('Tenha um bom dia! Dirija com segurança!')