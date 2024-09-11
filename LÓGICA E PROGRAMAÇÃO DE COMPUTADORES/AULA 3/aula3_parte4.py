# Programa que determina o preço de venda de um produto conforme custo dos produtos.

# Variável custo do produto
custo_prod = int(input("Informe o valor de custo do produto: "))
# Estrutura de condição
if custo_prod < 0:
    print("Produto com valor inexistente na tabela") 
else:
    # valor abaixo de R$10 = 70% de lucro
    if custo_prod <= 10:
        valor_venda = custo_prod * 1.7
    # valor entre R$10 e menor que R$30 = 50% de lucro
    if custo_prod >= 10 and custo_prod < 30:
        valor_venda = custo_prod * 1.5
    # valor a partir de R$30 e menor que R$50 = 40% de lucro
    if custo_prod > 30 and custo_prod < 50:
        valor_venda = custo_prod * 1.4
    # valor acima ou igual a R$50 = lucro de R$30
    if custo_prod >= 50:
        valor_venda = custo_prod * 1.3

    print("Valor para venda: ", valor_venda)
    



