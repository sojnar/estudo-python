n = 0
soma = 0
while n <= 10:
    valor = int(input(f'{n}º Numero digitado: '))
    soma = soma + valor
    n = n + 1
print('A media é', soma / 10)