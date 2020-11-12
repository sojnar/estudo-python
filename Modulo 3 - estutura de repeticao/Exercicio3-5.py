tabuada = 1
mult = 0
result = 0
while tabuada <= 10:
    print(f'Imprimindo a tabuada do {tabuada}')
    mult = 0
    while mult <= 10:
        result = tabuada * mult
        print(f'{tabuada} * {mult} = {result}')
        mult = mult + 1
    tabuada = tabuada + 1