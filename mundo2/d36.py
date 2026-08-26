"""
EXERCÍCIO D36 - Analizador de imprestimo
Crie um programa que:
1. pergunte ao usuário o valor da casa
2. pergunte o salário do comprador
3. pergunte em quantos anos ele vai pagar
4. calcule o valor da prestação mensal
5. se a prestação for maior que 30% do salário, exiba "Empréstimo negado"
6. caso contrário, exiba "Empréstimo aprovado"
"""

valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Digite em quantos anos o comprador pretende pagar: '))

meses = anos * 12
prestacao = valor / meses

if prestacao > salario * 0.3:
    print('Emprestimo Negado')
else:
    print('Emprestimo Aprovado')