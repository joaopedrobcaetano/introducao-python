cigarros_por_dia = int(input('Quantos cigarros você fuma por dia? '))
anos_fumando = int(input('Há quantos anos você fuma? '))
total_cigarros = cigarros_por_dia * anos_fumando * 365
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 1440
print(f'Você perdeu aproximadamente {dias_perdidos:.2f} dias de vida por fumar.')