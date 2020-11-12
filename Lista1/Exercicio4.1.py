#Calcula a porcentagem de aumento a partir 
#do novo salário

salario = float(input('Digite o salário atual: '))
salarioNovo = float(input('Digite o novo salário: '))
valorAumento = (salarioNovo - salario) 
porcentagem = (valorAumento/salario) * 100
print(f'O aumento foi de : R$ {valorAumento: .2f}')
print(f'Você teve um aumento de : R$ {porcentagem: .4f}%')

