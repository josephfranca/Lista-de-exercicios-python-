#Conversão de unidades de medida

# Implementar pelo menos uma conversão de unidades, por exemplo: 
# quilômetros para metros
# metros para centímetro

#Inserindo o valor em metros para ser convertido.
Metros = float(input("Digite um valor em metros para que seja convertido: "))

#Convertendo o valor para as outras unidades de medidas
Km = Metros / 1000
Cm = Metros * 100
Mm = Metros * 1000

#Exibindo o valor convertido em outras unidades de medidas
print("Em Km: ", Km)
print("Em cm: ", Cm)
print("Em mm: ", Mm)
