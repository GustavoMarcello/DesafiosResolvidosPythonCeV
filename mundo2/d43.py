"""
EXERCÍCIO D43 - Calculadora de IMC (Índice de Massa Corporal)
Crie um programa que:
1. Peça ao usuário para digitar seu peso (em kg) e altura (em metros)
2. Calcule o IMC usando a fórmula: IMC = peso / (altura ^ 2)
3. Classifique o IMC conforme a tabela:
   - IMC < 18.5: Abaixo do peso
   - 18.5 <= IMC < 25: Peso normal
   - 25 <= IMC < 30: Sobrepeso
   - IMC >= 30: Obesidade
4. Exiba o IMC e a classificação
"""

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'IMC: {imc} ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print(f'IMC: {imc} PESO NORMAL')
elif imc >= 25 and imc < 30:
    print(f'IMC: {imc} SOBREPESO')
else:
    print(f'IMC: {imc} OBESIDADE')
