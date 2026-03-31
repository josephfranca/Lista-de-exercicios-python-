# Programa para calcular a área de diferentes figuras geométricas

# Solicita ao usuário que escolha uma figura
Op = int(input("1-quadrado/2-retangulo/3-triangulo/4-circulo/ Escolha:"))

# Verifica qual opção foi escolhida
if Op == 1:
    # Cálculo da área do quadrado (lado²)
    Lado = float(input("Digite o lado:"))
    Area = Lado ** 2 

elif Op == 2:
    # Cálculo da área do retângulo (base x altura)
    Base = float(input("Digite a base:"))
    Altura = float(input("Digite a altura:"))
    Area = Base * Altura

elif Op == 3: 
    # Cálculo da área do triângulo (base x altura / 2)
    Base = float(input("Digite a base:"))
    Altura = float(input("Digite a altura:"))
    Area = Base * Altura / 2

elif Op == 4:
    # Cálculo da área do círculo (π x raio²)
    Raio = float(input("Digite o raio:"))
    Area = 3.14 * (Raio ** 2)

else:
    # Caso o usuário digite uma opção inválida
    print("Opção inválida!")
    Area = None  # Define área como vazia

# Exibe o resultado final
print("Área:", Area)