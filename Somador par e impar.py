soma = 0
cont = 0
somaImpar = 0

while cont < 10:
    Valor = float(input("Digite valor: "))
    if Valor % 2 == 0: # Verificando o resto da divisão para identificar os números pares
        soma = soma + Valor # Acumulando e somando valores
    elif Valor % 2 == 1: #Verificando o resto da divisão para identificar os números impares
        somaImpar = somaImpar + Valor
        cont = cont + 1 # Contador do while
    
    print("\n A soma dos números pares é: ", soma)
    print("\n  A soma dos números impares é ", somaImpar)
    