# Cálculo de porcentagem

# O programa deve calcular uma porcentagem de um valor informado pelo

# usuário (ex.: calcular 10% de um valor).

# O python não tem o try catch mas tem o try except, que na prática é a mesma coisa

# O try catch (ou try except no caso do python), serve como uma especie de verificação
# O bloco try tenta executar o que está dentro do comando.
# Já o catch (ou expect no python), é acionado caso algo dê errado, como se fosse um if e else 
# Usei o while como forma de validação, porque caso entrasse no except ele travava e a forma que eu encontrei pra burlar isso foi colocando o código em loop infinito com um break dps do resultado ser imprimdo.


while True: 
    try:
    #Pedindo o primeiro valor para o usuário
        Valor = float(input("Digite um valor: R$ "))
        #Pedindo a porcentagem
        Porcentagem = float(input("Digite a porcentagem (%): "))
        # Operação para obter a porcentagem
        Resultado = (Porcentagem / 100) * Valor
        #Exibindo de forma formatada
        print(f"{Porcentagem}% de R$ {Valor:.2f} é igual a R$ {Resultado:.2f}")
        break
    except ValueError:
        print("Erro, digite apenas a números!")
