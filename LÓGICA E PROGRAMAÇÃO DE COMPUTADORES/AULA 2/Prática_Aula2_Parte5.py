import math
# CONVERSOR FAHRENHEIT PARA CELSIUS

print("Informe a temperatura em Fahrenheit:")
f = int(input())
c = 5/9*(f-32)
print("A temperatura em Celsius é", c)

# PROGRAMA QUE LÊ DOIS VALORES INTEIROS E ESCREVE NA TELA:
# A SOMA

print("DIGITE UM VALOR:")
a = int(input())
print("DIGITE OUTRO VALOR:")
b = int(input())
print("A SOMA DOS VALORES É:", a+b)
# A DIFERENÇA
print("A DIFERENÇA DOS VALORES É:", a-b)
# A MÉDIA
print("A MÉDIA DOS VALORES É:", (a+b)/2)
# A DISTÂNCIA
print("A DISTÂNCIA DOS VALORES É:", math.fabs(a-b))
# O MAIOR DOS DOIS
print("O MAIOR DOS VALORES É:", (a+b+math.fabs(a-b))/2)
# O MENOR DOS DOIS
print("O MENOR DOS VALORES É:", (a+b-math.fabs(a-b))/2)

