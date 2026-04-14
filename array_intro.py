#Declarando o array de float
lista = [4.0, 9.2, 3.1, 9.1, 1.5, 3.2, 2.6]
#Imprimindo todos os valores do array
print("A lista criada é ", lista)
#Imprimindo o primeiro elemento do array
print("O 1º elemento da lista é ", lista[0])
#Imprimindo o último valor, len é equivalente a lenght do javascript
print("O último elemento da lista é ", lista[len(lista)-1] )

#Criando o acumulador
soma = 0
#For que vai até o final dos indices do array lista
for i in range(len(lista)):
    soma += lista[i]
print("A soma dos elementos da lista é ", soma)
print("Os elementos nas posições pares da lista são:")
#For que vai passando apenas nos indices pares, 0, 2, 4, 6
for i in range(0,len(lista),2):
    print(lista[i])