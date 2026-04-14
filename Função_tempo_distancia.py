#Função utilizando dois parâmetros para velocidade e tempo
def velocidade(s,t):
    #Validação de tempo
    if t > 0:
        v = s/t
        return (v)
    else:
        return (0)
    
#Pedindo dados para os parâmetros
s = float(input("Digite a distância percorrida pelo objeto, em Km: "))
t = float(input("Digite o tempo transcorrido, em horas: "))
#Chamando a função e colocando os dados digitados como parâmetros
res = velocidade(s,t)
#Validação da resposta, se o calculo da função retornar zero ou negativo, entrará no else.
if res != 0:
    print("A velocidade do objeto é ", res , " Km/h")
else:
    print("Você digitou zero para o tempo ou para a distância")