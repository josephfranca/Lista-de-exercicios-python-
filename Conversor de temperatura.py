#Conversor de temperatura
temperatura = int(input("Escolha uma das seguintes opções: 1-Celsius para Fahrenheit 2-Fahrenheit para Celsius"))
#Celsius → Fahrenheit
if temperatura == 1:
    c = float(input("Digite a temperatura(em Celcius) que deseja converter(para Fahrenheit):"))
    result = (c * 9/5) + 32
#Fahrenheit → Celsius
elif temperatura == 2:
    f = float(input("Digite a temperatura(em Fahrenheit) que deseja converter(para Celcius):"))
    result = (f - 32) * 5/9
#Outra opção
else:
    print("Opção inválida")
    result = None
#Resultado
if result != None:
    print("Resultado:", result)

