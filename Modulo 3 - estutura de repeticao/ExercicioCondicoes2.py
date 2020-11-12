#Empresa de telefonia
# < 200 = 0,20
# >= 200 and <= 400 = 0,18
# > 400 = 0,15

minutos = int(input("Digite o tempo em minutos da ligação: "))
if minutos < 200:
    valor = minutos * 0.20
elif minutos <= 400:
    valor = minutos * 0.18
elif minutos <=800:
    valor = minutos * 0.15
else:
    valor = minutos * 0.08    
print(f"O valor a ser pago é de R${valor: .2f}")