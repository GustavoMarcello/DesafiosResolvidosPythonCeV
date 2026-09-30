"""
# Video com os desafios:  CeV Python POO: Aula 15 https://www.youtube.com/watch?v=PAGg0NgeMX4&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=36

EXERCÍCIO D36 - Simulador de diferentes tipos de pagamentos
Crie um programa que:
1. Contenha a classe abstrata Pagamento contendo:
    - __valor
    - @fvalor: property retornando valor formatado em R$ 0,00
    - pagar() - abstractmethod
2. Crie as classes Boleto, Credito e Pix que herdam de Pagamento
3. Implemente o método pagar() de acordo com a regra:
    - Boleto: "Pagando valor de R$ {fvalor} via Boleto"
    - Credito: "Pagando valor de R$ {fvalor} via Cartão de Crédito"
    - Pix: "Pagando valor de R$ {fvalor} via Pix"
"""