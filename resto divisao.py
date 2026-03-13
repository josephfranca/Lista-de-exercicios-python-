#Faça um programa que leia dois números reais e imprima o resto da divisão
#de um pelo outro.

#pedindo que o usuário digite os dois números que ficaram salvos nas variáveis
n1 = float(input("Digite um número: "))

n2 = float(input("Digite outro número: "))

# Variável que vai ficar armazenada o resto
resto = n1 % n2
# Variável que fica o resultado total da divisão, optei por exibir o resultado também
resultado = n1 / n2

#Exibindo na tela
print("A divisão de: ", n1, "E ", n2, " Resulta em: ", resultado, " e o resto da divisão é:  ", resto) 