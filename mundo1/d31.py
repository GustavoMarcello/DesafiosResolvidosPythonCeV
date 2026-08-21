"""
EXERCÍCIO D31 - Cálculo de Preço de Passagem por Distância
Crie um programa que:
1. Peça ao usuário para digitar a distância total da viagem em km
2. Aplique uma tabela de preços:
   - Se a distância for até 200 km: R$ 0.50 por km
   - Se for maior que 200 km: R$ 0.45 por km
3. Calcule e exiba o preço total da passagem
"""

distTotal = float(input('Digite a distância total da viagem em km: '))

if distTotal <= 200:
    print(f'Valor total da passagem: R$ {distTotal*0.5}')
else:
    print(f'Valor total da passagem: R$ {distTotal*0.45}')