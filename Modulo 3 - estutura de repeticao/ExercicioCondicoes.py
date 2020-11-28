#Pergunte a velocidade de um carro, supondo um valor inteiro.
#Caso ultrapasse 110 km/h, exiba uma mensagem dizendo que o usuário
#foi multado. Neste caso, exiba o valor da multa, cobrando R$5,00
#por km acima de 110

velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 110:
    valorUltrap = velocidade - 110
    totalMulta = float(valorUltrap * 5)
    print(f"O valor a ser pago é de {totalMulta: .2f}")
else:
    print("Você andou dentro da lei!")