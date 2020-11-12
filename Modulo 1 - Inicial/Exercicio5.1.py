#Calcular o valor gasto de gasolida a partir da viagem percorrida
#E o tempo de viagem

distancia = float(input('Digite a distancia a ser percorrida em KM: '))
velocidade = float(input('Digite a velocidade media da viagem em KM/h: '))
valorGasolina = float(input('Digite o  valor da gasolina: '))
kmPorLitro = float(input('Digite quantos km o seu veiculo faz por litro: '))
abastecimento = distancia / kmPorLitro
valorGasolina = abastecimento * valorGasolina
tempo = distancia / velocidade
print(f'O tempo da viagem será de {tempo: .0f} hora aproximadamente')
print(f'Você gastara R${valorGasolina: .2f} nessa viagem e tera que abastecer {abastecimento: .2f} Litros')