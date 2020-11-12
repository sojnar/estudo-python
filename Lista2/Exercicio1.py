ladoA = int(input('Digite o lado a: '))
ladoB = int(input('Digite o lado b: '))
ladoC = int(input('Digite o labo c: '))
if ladoA > ladoB + ladoC or ladoB > ladoA + ladoC or ladoC > ladoA + ladoB:
    print("Não pode ser um triangulo")
    print("Um dos lados é maior que a soma dos outros")
elif ladoA == ladoB == ladoC:
    print('equilátero')
elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
    print('Isósceles')
else:
    print('Escaleno')