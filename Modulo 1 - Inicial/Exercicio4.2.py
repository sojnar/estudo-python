## Calcula o valor Total do produto após passar a porcentagem

valorProduto = float(input('Digite o valor do produto: '))
descPorcento = float(input('Digite o desconto em %: '))
valorDesc = valorProduto * descPorcento / 100
valorTotal = valorProduto - valorDesc
print(f'Valor dos desconto : R$ {valorDesc: .2f}')
print(f'Valor total: R$ {valorTotal: .2f}')