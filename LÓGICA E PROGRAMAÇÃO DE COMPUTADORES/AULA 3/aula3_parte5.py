# Programa que lê um valor inteiro de  1 a 7, correspondente ao dia da semana.
# O programa deve escrever o dia da semana por extenso correspondente ao valor lido

# Definição da variável que capta o valor digitado pelo usuário
dia_da_semana = int(input("Digite um valor de 1 a 7: "))
# Estrutura condicional
if (dia_da_semana < 1 or dia_da_semana > 7):
    print("Valor digitado não existe! Verifique as opções.")
else:
    if (dia_da_semana == 1):
        print("Domingo")
    if (dia_da_semana == 2):
        print("Segunda")
    if (dia_da_semana == 3):
        print("Terça")
    if (dia_da_semana == 4):
        print("Quarta")
    if (dia_da_semana == 5):
        print("Quinta")
    if (dia_da_semana == 6):
        print("Sexta")
    if (dia_da_semana == 7):
        print("Sábado")
# Programa que lê 3 notas, calcula a média ponderada considerando peso 5 para a maior nota e peso 2.5 para as subsequentes.

# Captando dados do usuário via input
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
# Estrutura condicional
if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10) or (nota3 < 0 or nota3 > 10):
    print("Erro")
else:
    nota_maior = nota1
    if (nota2 > nota1):
        nota_maior = nota2
    if (nota3 > nota2):
        nota_maior = nota3
    if nota1:
        nota1 *= 0.5
    if nota2:
        nota2 *= 0.25
    if nota3:
        nota3 *= 0.25
# Cálculo média ponderada
media_ponderada = (nota1 + nota2 + nota3)
print("A média ponderada é: ", media_ponderada)

# Programa que lê valores a,b e c de uma fórmula de bhaskara, calcule e escreva suas raízes reais
import math
# Captando os valores a,b e c do usuário
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

delta = math.pow(b,2) - 4 * a * c
if (delta < 0 or a == 0):
    print("Erro, valores negativos não são calculáveis")
else:
    x1 = (-b + math.sqrt(delta)//(2 * a))
    x2 = (-b - math.sqrt(delta)//(2 * a))
    print("X1: ", x1)
    print("X2: ", x2)

# Programa que recebe o valor do saldo médio de um conta corrente, calcula e escreve o seu limite conforme a tabel abaixo
# Menor que R$500 = NÃO HÁ LIMITE
# Entre R$500 e R$1000 = 8% do saldo médio
# Maior ou igual a R$1000 = 15% do saldo médio

# Captando dado do usuário
saldo_medio = float(input("Informe seu saldo: "))

if (saldo_medio < 500):
    print("Ops! Você não tem limite")
if (saldo_medio > 500 or saldo_medio < 1000):
    limite = (saldo_medio * 0.8)
    print("Limite é de: ", limite)
if (saldo_medio > 1000):
    limite = (saldo_medio * 0.15)
    print("Limite é de: ", limite)
