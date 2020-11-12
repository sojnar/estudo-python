###Calcula o valor do salario a partir da porcentagem passada
salario = float(input('Digite o salário atual: '))
porcentagem = float(input('Digite o aumento em %: '))
aumento = salario * porcentagem / 100
novoSalario = salario + aumento
print(f'Aumento : R$ {aumento: .2f}')
print(f'Novo salário: R$ {novoSalario: .2f}')

