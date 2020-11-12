nome = input('Ditige um nome: ')
n1 = float(input('Digite a nota da N1: '))
n2 = float(input('Digite a nota da N2: '))
media = (n1 + n2) / 2
print(media)
if media < 7:
    print(f'Aluno {nome} Reprovado')
else:
    print(f'Aluno {nome} Aprovado')