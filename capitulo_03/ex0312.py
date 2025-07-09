distancia = float(input('Qual será a distância a ser percorrida em km? '))
velocidade_media = float(input('Qual será a velocidade média do veículo em km/h? '))
tempo = distancia / velocidade_media
print(f'O tempo estimado para percorrer {distancia:.2f} km a uma velocidade média de {velocidade_media:.2f} km/h é de {tempo:.2f} horas.')