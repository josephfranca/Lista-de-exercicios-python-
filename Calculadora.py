while True:
    print("\n === Calculadora ===")
    print("1 - Soma")
    print("2 - Substração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        print("Encerrando")
        break
    
    if opcao in ["1","2","3","4"]:
        Num1 = float(input("Digite o primeiro número: "))
        Num2 = float(input("Digite o segundo número: "))
        
        if opcao == "1":
            Resultado = Num1 + Num2
            print("Resultado de sua soma: ", Resultado)
            
        elif opcao == "2":
            Resultado = Num1 - Num2
            print("Resultado de sua subtração: ", Resultado)
            
        elif opcao == "3":
            Resultado = Num1 * Num2
            print("Resultado de sua multiplicação: ", Resultado) 
            
        elif opcao == "4":
            if Num2 != 0:
                Resultado = Num1 / Num2
                print("Resultado de sua divisão: ", Resultado)
        else:
            print("Erro: divisão por zero não é permitida")
    else:
        print("Erro, valor digitado incorretamente.")