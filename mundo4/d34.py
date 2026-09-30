"""
# Video com os desafios:  CeV Python POO: Aula 15 https://www.youtube.com/watch?v=PAGg0NgeMX4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=36

EXERCÍCIO D34 - Bônus Salarial
Crie um programa que:
1. Contenha a classe abstrata Funcionario contendo:
    - nome
    - __salario
        - Implemente get e set para o atributo __salario
        - Colocar validação no set para que o salário não seja negativo nem menor que o salario atual
    - calcular_bonus_salarial() - abstrato
2. Crie as classes Gerente, Designer e Desenvolvedor que herdam de Funcionario
3. Implemente o método calcular_bonus_salarial() de acordo com a regra:
    - Gerente: 15% do salário
    - Designer: 8% do salário
    - Desenvolvedor: 10% do salário
4. Implemente um print com nome, salário e bônus ao criar o objeto.
"""