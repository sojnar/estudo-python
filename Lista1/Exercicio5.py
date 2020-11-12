#Calcular o tempo de viagem baseado na distancia/velocidade

distancia = float(input('Digite a distancia a ser percorrida em KM: '))
velocidade = float(input('Digite a velocidade media da viagem em KM/h: '))
tempo = distancia / velocidade
print(tempo)
print(f'O tempo da viagem será de {tempo: .0f} hora aproximadamente')