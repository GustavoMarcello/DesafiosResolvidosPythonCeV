"""
EXERCÍCIO D73 - Tuplas com Times de Futebol
Crie um programa que:
1. Crie uma tupla com os nomes dos times do Brasileirão 2026
2. Exiba os 5 primeiros times
3. Exiba os últimos 4 times
4. Exiba os times em ordem alfabética
5. Exiba a posição do time "Flamengo"
"""

times = (
    "Palmeiras",
    "Flamengo",
    "Atlético-PR",
    "Fluminense",
    "Cruzeiro",
    "Bahia",
    "Bragantino",
    "Coritiba",
    "Atlético-MG",
    "Corinthians",
    "Botafogo",
    "Vitória",
    "São Paulo",
    "Santos",
    "Grêmio",
    "Internacional",
    "Mirassol",
    "Remo",
    "Vasco",
    "Chapecoense"
)

# 1. Exibir todos os times
print("Times do Brasileirão 2026:")
print(times)

# 2. Exibir os 5 primeiros times
print("\n5 primeiros times:")
print(times[:5])

# 3. Exibir os últimos 4 times
print("\nÚltimos 4 times:")
print(times[-4:])

# 4. Exibir os times em ordem alfabética
print("\nTimes em ordem alfabética:")
print(sorted(times))

# 5. Exibir a posição do Flamengo
posicao = times.index("Flamengo") + 1
print("\nPosição do Flamengo:", posicao)