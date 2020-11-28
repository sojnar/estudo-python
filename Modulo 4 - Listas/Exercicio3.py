total = []
soma = 0
count = 0
while count < 4:
    total.append(float(input("Ditite a nota do aluno: ")))
    soma = soma + total[count]
    count = count + 1
print(soma)
media = soma / len(total)
print(media)