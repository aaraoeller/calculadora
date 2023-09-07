print('''Suas opções:
[ 1 ] Área de um Quadrado
[ 2 ] Perímetro de um Quadrado
[ 3 ] Área de um Círculo
[ 4 ] Perímetro de um Círculo
''')

tipo_calculo = int(input('Selecione qual o tipo de cálculo você deseja: '))

if tipo_calculo == 1:
    
    n1 = float(input(f"Digite o valor do lado do Quadrado: "))

    area_quadrado = (n1 * n1)

    print(f"A área é: {area_quadrado:.1f}")

elif tipo_calculo == 2:
    
    n1 = float(input(f"Digite o valor do lado do Quadrado: "))

    perimetro_quadrado = (4 * n1)

    print(f"O perímetro é: {perimetro_quadrado:.1f}")

elif tipo_calculo == 3:
    
    n3 = float(input("Digite o valor do raio do Círculo: "))

    area_circulo = (3.14159 * n3 * n3)

    print(f"A área do Círculo é: {area_circulo:.1f}")

elif tipo_calculo == 4:

    n4 = float(input("Digite o valor do raio do Círculo: "))

    perimetro_circulo = (2 * 3.14159 * n4)

    print(f"O perímetro do Círculo é: {perimetro_circulo:.1f}")

else:
    print("Ação inválida")