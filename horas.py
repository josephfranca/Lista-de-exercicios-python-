# Faça um programa que leia dois valores inteiros representando,
# respectivamente, um valor de hora e um de minutos e informe quantos
# minutos se passaram desde o início do dia. Exemplo:

# valores lidos: 13 e 15

# impressão: 795 minutos


horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))


calculo = (horas * 60) + minutos

print(calculo)