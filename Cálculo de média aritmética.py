# Cálculo de média aritmética

# O programa deve solicitar ao usuário um conjunto de números (por

# exemplo, três ou quatro notas) e calcular a média aritmética

#Print só para exibir essa mensagem no console quando estiver em execução
print("Programa para notas escolares")

#Declarando as variáveis onde ficará salvo os valores das notas
N1 = float(input("Digite a primeira nota: "))

#Sistema de verificação/validação para não inserir um valor inválido.
if(N1 < 0 or N1 > 10 ):
    print("Valor inválido, digite um número maior que zero e menor que 10: ")
    N1 = float(input("Digite a primeira nota: "))

N2 = float(input("Digite a segunda nota: "))

if(N2 < 0 or N2 > 10):
    print("Valor inválido, digite um número maior que zero e menor que 10: ")
    N2 = float(input("Digite a segunda nota: "))
    
N3 = float(input("Digite a terceira nota: "))

if(N3 < 0 or N3 > 10):
    print("Valor inválido, digite um número maior que zero e menor que 10: ")
    N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a última nota: "))

if(N4 < 0 or N4 > 10):
    print("Valor inválido, digite um número maior que zero e menor que 10: ")
    N4 = float(input("Digite a última nota: "))
    
#Operação para calcular a média
Media = (N1 + N2 + N3 + N4) / 4

#Exibindo na tela cada nota e média final 
print("A primeira nota foi: ", N1)
print("A segunda nota foi: ", N2)
print("A terceira nota foi: ", N3)
print("A quarta nota foi: ", N4)
print("A média final é: ", Media)

if(Media >= 5):
    print("Aluno aprovado, parábens! ")
else:
    print("Aluno reprovado, mais atenção na próxima tentativa.")
