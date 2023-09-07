import math

print('''Suas opções:
[ 1 ] Área de um Quadrado
[ 2 ] Perímetro de um Quadrado
[ 3 ] Área de um Círculo usando o Raio
[ 4 ] Perímetro de um Círculo
[ 5 ] Raio de um Círculo
[ 6 ] Área de um Círculo usando o Diâmetro
[ 7 ] Metade da Área de um Círculo
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

    area_circulo = (3.14 * n3 * n3)

    print(f"A área do Círculo é: {area_circulo:.1f}")

elif tipo_calculo == 4:

    n4 = float(input("Digite o valor do raio do Círculo: "))

    perimetro_circulo = (2 * 3.14 * n4)

    print(f"O perímetro do Círculo é: {perimetro_circulo:.1f}")

elif tipo_calculo == 5:
    
    n5 = float(input("Digite o valor da área do Círculo: "))

    raio_circulo = (n5 / 3.14)
    raiz_quadrada = math.sqrt(raio_circulo)

    print(f"O raio do Círculo é: {raiz_quadrada:.1f}")

elif tipo_calculo == 6:

    n6 = float(input("Digite o valor do Diâmetro do Círculo: "))

    diam_circulo = (n6 / 2)
    calc_diam = (diam_circulo * diam_circulo * 3.14 )

    print(f"A Área do Círculo é: {calc_diam:.1f}")

elif tipo_calculo == 7:

    n7 = float(input("Digite o diâmetro do Círculo: "))

    diametro_circulo = (n7 / 2)
    calc_diametro = (diametro_circulo * diametro_circulo * 3.14 )
    metade_area = (calc_diametro / 2)

    print(f"A metade da área do Círculo é: {metade_area:.1f}")

else:
    print("Ação inválida")