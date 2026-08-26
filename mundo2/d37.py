"""
EXERCÍCIO D37 - Conversor de Números Entre Bases
Crie um programa que:
1. Peça ao usuário para digitar um número inteiro
2. Converta esse número para diferentes bases:
   - Binário (base 2)
   - Octal (base 8)
   - Hexadecimal (base 16)
3. Exiba o número original e suas representações em cada base
"""

n = int(input('Digite um Número: '))

print(f'Converter {n} para BINARIO: {bin(n)}')
print(f'Converter {n} para OCTAL: {oct(n)}')
print(f'Converter {n} para HEXADECIMAL: {hex(n)}')