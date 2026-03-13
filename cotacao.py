# 'Faça um programa que leia a cotação do dólar (taxa de conversão), leia um
# valor em dólares e converta e mostre o valor equivalente em Reais.'

#Inserindo o valor da cotação do dia
cotacao = float(input("Digite o valor da cotação atual do dolar: "))
#Inserindo o valor que deseja converter
Dolar = float(input("Digite o valor que deseja converter em reais: "))

#Operação salva na variável real
real = cotacao * Dolar
#Print final com o valor que foi convertido e quando ficou em reais
print("O valor convertido de: ", Dolar, " é de : ", real, " Reais")