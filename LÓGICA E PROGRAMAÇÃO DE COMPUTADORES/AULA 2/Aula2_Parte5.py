# AULA 2 PARTE 5
import math

# CONVERSOR FAHRENHEIT PARA CELSIUS
print("Informe a temperatura em Fahrenheit:")
f = int(input())
c = 5/9*(f-32)
print("A temperatura em Celsius é", c, "\n")

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
print("O MENOR DOS VALORES É:", (a+b-math.fabs(a-b))/2, "\n")

# PROGRAMA QUE LÊ O TEMPO DE UM EVENTO EM SEGUNDOS E O ESCREVE DECOMPOSTO EM HORAS, MINUTOS E SEGUNDOS
print("INFORME O TEMPO DO EVENTO EM SEGUNDOS:")
tempo = int(input())
horas = tempo//3600
print("Horas: ", horas)
resto = tempo%3600
minutos = resto//60
print("Minutos: ", minutos)
segundos = resto%60
print("Segundos: ", segundos, "\n")

# PROGRAMA QUE LÊ UM VALOR INTEIRO DE 4 DÍGITOS E O DEVOLVE EM ORDEM INVERSA
print("DIGITE UM VALOR COM 4 DÍGITOS:")
valor = int(input())
milhar = valor//1000
resto = valor%1000
centena = resto//100
resto = resto%100
dezena = resto//10
unidade = resto%10
print("VALOR DIGITADO: ", valor)
print("VALOR INVERTIDO: ", unidade*1000 + dezena*100 + centena*10 + milhar)


