"""
# Video com os desafios:  CeV Python POO: Aula 15 https://www.youtube.com/watch?v=PAGg0NgeMX4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=36

EXERCÍCIO D35 - Simulador de abertura de arquivos
Crie um programa que:
1. Contenha a classe abstrata Arquivo contendo:
    - nome
    - _extensao
    - tamanho (em bytes)
    - @nomecompleto: property retornando 'nome + extensao + tamanho'
    - abrir() - abstractmethod
2. Crie as classes PDF e DOC que herdam de Arquivo
3. Implemente o método abrir() de acordo com a regra:
    - PDF: "Abrindo arquivo PDF de tamanho {tamanho} Mb no Navegador"
    - DOC: "Abrindo arquivo DOC de tamanho {tamanho} Mb no Word"
"""