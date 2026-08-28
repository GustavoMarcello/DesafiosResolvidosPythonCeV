"""
EXERCÍCIO D76 - Tuplas com Preços
Crie um programa que:
1. Crie uma tupla com os nomes e preços de vários produtos
2. Exiba uma listagem de preços formatada
"""

produtos = (
    ("Arroz", 25.90),
    ("Feijão", 8.50),
    ("Macarrão", 5.99),
    ("Leite", 4.79),
    ("Café", 18.90),
    ("Açúcar", 4.50)
)

print("-" * 30)
print("        LISTA DE PREÇOS")
print("-" * 30)

for produto, preco in produtos:
    print(f"{produto:<15} R$ {preco:>6.2f}")

print("-" * 30)