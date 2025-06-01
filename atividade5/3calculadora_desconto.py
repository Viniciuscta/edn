"""
Crie um programa que receba o preço original de um produto e um percentual de desconto,
realizando o cálculo do preço final após a aplicação do desconto.
"""
# Definição da função
def calculadora_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final


# Input do usuário
preco_original = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))

# Calculo do desconto
preco_com_desconto = calculadora_desconto(preco_original, desconto)

# Saída de dados
print(f"O preço final com {desconto}% de desconto é: R$ {preco_com_desconto:.2f}.")