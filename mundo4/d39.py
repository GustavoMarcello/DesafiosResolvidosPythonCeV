"""
# Video com os desafios:  CeV Python POO: Aula 15 https://www.youtube.com/watch?v=PAGg0NgeMX4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=36

EXERCÍCIO D39 - Validadores de dados
Crie um programa que:
1. Contenha a classe abstrata Validador contendo:
    - validar() - abstractmethod
2. Crie as classes Email, Usuario e Senha que herdam de Validador
3. Implemente o método validar() com metodos de regex:
    - Email:
        - conter @ e .com
        - não possuir caracteres especiais

    - Usuario:
        - 5 a 20 caracteres
        - não possui caracteres especiais
        
    - Senha: 
        - validar se a senha tem entre 8 e 20 caracteres
        - possui letras maiúsculas, minúsculas
        - números e caracteres especiais
"""