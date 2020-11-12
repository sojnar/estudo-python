#Converter dias, horas, minutos, segundos
#para segundos

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

total = dias*24*60*60 + horas*60*60 + minutos*60 + segundos
print(f'O total de segundos é {total} ')