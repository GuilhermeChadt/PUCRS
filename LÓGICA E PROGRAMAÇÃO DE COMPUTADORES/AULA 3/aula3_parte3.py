# SELEÇÃO COMPOSTA (IF/ELSE)
# Programa que lê o tempo de duração de um jogo

hora_inicio = int(input("Informe a hora de início do jogo: "))
minuto_inicio = int(input("Informe os minutos: "))
hora_fim = int(input("Informe a hora final do jogo: "))
minuto_fim = int(input("Informe o minuto final."))
horario_inicial = (hora_inicio * 60) + minuto_iniciohorario_final = (hora_fim * 60) + minuto_fim

if horario_inicial < horario_final:
    duracao_jogo = (horario_final - horario_inicial)
else:
    duracao_jogo = (24 * 60 - horario_final + horario_inicial)
   
print("Horas: ", duracao_jogo//60)
print("Minutos: ", duracao_jogo%60)

# Programa que lê um número inteiro de 4 dígitos e garanta essa condição, deve determinar se um número é capicua.

valor = int(input("Digite um número de 4 dígitos: "))

if valor <= 1111 or valor >=9999:
    print("Valor inválido, refaça a operação seguindo as condições propostas!")
else:
    milhar = valor/1000
    resto = valor%100  
    resto = resto%100
    dezena = resto//10
    unidade = resto%10
    valor_invertido = (unidade*100 + dezena*100 + centena*10 + milhar)
    if valor_invertido == valor:
        print("Valor informado é capicua")
    else:
        print("Valor informado não é capicua!")
