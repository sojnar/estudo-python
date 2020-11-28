soma = 0
cont = 0
while True:
    x = int(input('Insira um ou (zero para sair): '))
    if x == 0:
        break
    soma = soma + x
    cont = cont + 1
print(f'Soma: {soma / cont}')