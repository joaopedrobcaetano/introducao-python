velocidade = int(input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade - 80) * 5
    print(f"Valor da multa: R$ {multa:.2f}")
if velocidade <= 80:
    print("Sua velocidade está ok, boa viagem!")