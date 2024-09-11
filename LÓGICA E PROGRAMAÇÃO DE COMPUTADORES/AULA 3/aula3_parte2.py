# CODIFIQUE UM PROGRAMA QUE LEIA UM VALOR INTEIRO E INDIQUE SE O VALOR É POSITIVO, NEGATIVO OU ZERO

valor = int(input("Informe um valor: "))
if valor < 0:   
    print("O valor digitado é negativo.", valor)
if valor > 0:
    print("\nO valor digitado é positivo.", valor)
if valor == 0:
    print("\nO valor digitado é igual a zero.", valor)

# Leia a altura e gênero e indique seu peso ideal
# 1 para FEMININO: 62.1 x ALTURA - 44.7
# 2 para MASCULINO: 72.7 x ALTURA - 58

altura = float(input("Informe sua altura: "))
genero = int(input("\nInforme seu gênero, digite 1 para Feminino ou 2 para Masculino: "))

if genero == 1:
    Peso_Ideal = 66.2 * altura - 44.7
    print("Seu peso ideal é: ", Peso_Ideal)
if genero == 2:
    Peso_Ideal = 72.7 * altura - 58
    print("Seu peso ideal é: ", Peso_Ideal)
if genero != 1 and genero != 2:
    print("Seleção de gênero incorrecta, por favor refaça a operação respeitando as opções válidas.")

