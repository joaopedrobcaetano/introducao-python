km_percorridos = float(input('Digite a distância percorrida em km: '))
dias = int(input('Digite o número de dias pelos quais o carro foi alugado: '))
preco_total = (60 * dias) + (0.15 * km_percorridos)
print(f'O preço total a pagar pelo aluguel do carro é de R$ {preco_total:.2f}.')