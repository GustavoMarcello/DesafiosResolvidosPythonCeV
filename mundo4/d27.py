"""
# Video com os desafios:  CeV Python POO: Aula 09 https://www.youtube.com/watch?v=Qcsftqx36d4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=19

EXERCÍCIO D27 - Hernça RPG
Crie um programa que:
1. Contenha a classe abstrata Personagem contendo:
    - nome
    - vida
    - golpes
    - escolherAtaque() - retorna lista de opções de ataque
    - receberDano(dano)
    - usarPocao()
2. Crie classes filhas:
    - Guerreiro - ['Atacar com arma', 'Arremeçar adaga']
    - Mago - ataques ['Magic missles', 'fireball']
"""

from d27modules.mago import Mago
from d27modules.guerreiro import Guerreiro

jaina = Mago('Jaina Proudmore', 35, ['Magic missles', 'fireball'])
garrosh = Guerreiro('Garrosh Grito Infernal', 48, ['Atacar com arma', 'Arremeçar adaga'])

print(f'Vida Jaina: {jaina.vida}')
print(f'Vida Garrosh: {garrosh.vida}')
# jaina.fireball(garrosh)
garrosh.ataqueComArma(jaina)
jaina.usarPocao()
jaina.usarPocao()
jaina.usarPocao()
# garrosh.ataqueComArma(jaina)
# jaina.fireball(garrosh)
# garrosh.ataqueComArma(jaina)


