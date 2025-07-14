energia_consumida = float(input("Digite a energia consumida em kWh: "))
tipo_instalacao = input("Digite o tipo de instalação: [R] Residencial / [C] Comercial / [I] Industrial: ")
if tipo_instalacao == "R":
    if energia_consumida <= 500:
        valor = energia_consumida * 0.40
    else:
        valor = energia_consumida * 0.65
elif tipo_instalacao == "C":
    if energia_consumida <= 1000:
        valor = energia_consumida * 0.55
    else:
        valor = energia_consumida * 0.60
elif tipo_instalacao == "I":
    if energia_consumida <= 5000:
        valor = energia_consumida * 0.55
    else:
        valor = energia_consumida * 0.60
else:
    print("Tipo de instalação inválido.")
    valor = 0
print(f"O valor a pagar é: R${valor:.2f}")