# Faça um programa que leia um valor representando o gasto realizado por um
# cliente do restaurante ComaBem e visualize o valor total a ser pago,
# considerando os 10% do garçom.

gasto = float(input("Digite o valor gasto no restaurante: "))
porcentagem = 10

taxa_garcom = gasto * porcentagem / 100

print("Total com taxa do garçom: ", gasto + taxa_garcom , " caso queira retirar a gorjeta, ficará: ", gasto)