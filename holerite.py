#Faça um programa em python que 
#Obtenha um valor para variável ht (Horas trabalhadas no mês)
#Obtenha um valor para variável vh (Valor hora trabalhada)
#Obtenha um valor para variável PD (Percentual de desconto)
#calcule o salario bruto => SB = ht * vh
#Calcule o total de descontos => TD = (PD/100) * SB
#Calcule o salário liquido => sl = sb - td
#apresente os valores de horas trabalhadas, salário bruto, desconto e salario liquido

ht = int(input("Digite as horas trabalhadas: "))
vh = float(input("Digite o valor das horas trabalhadas: "))
pd = float(input("Digite o valor percentual dos descontos: "))
sb = ht * vh
td = (pd/100) * sb
sl = sb - td

print("Horas trabalhadas esse mês: ", ht)

print("Salário bruto: ", sb)

print("Valor percentual de descontos: ", pd)

print("Valor a receber (Salário líquido): ", sl)