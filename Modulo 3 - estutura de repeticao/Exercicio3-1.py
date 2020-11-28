#imprima os números pares de 0 até um número lido

cont = int(input("Digite o valor que deseja contar: "))
x = 0
while x <= cont:
    validaNum = x % 2
    if validaNum == 0:
        print(x)
    x = x + 1