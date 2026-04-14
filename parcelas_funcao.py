#Criando a função para calcular
def Parcelas(valor, qtde):
    res = (valor + 0.05*valor) / qtde
    return(res)

#Solicitando o valor 
valor = float(input("Digite o valor da compra R$: "))
#Solicitando o número de parcelas 
qtdeParcela = int(input("Digite a quantidade de parcelas: "))

#Imprimindo e usando os parâmetros da função, valor e qtde
print("Valor das parcelas: R$ ", Parcelas (valor,qtdeParcela))

#Programa que le o valor de uma compra e quantidade de parcelas, e calcula e imprime o valor das parcelas, toda compra que for parcelada terá 5% de juros.
