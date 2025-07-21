from decimal import Decimal

valor = Decimal(input("Digite o valor a pagar: R$ "))
cedulas_moedas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas_moedas += 1
    else:
        if cedulas_moedas != 0:
            print(f"{cedulas_moedas} cédula(s)/moeda(s) de R$ {atual}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = Decimal('0.50')
        elif atual == Decimal('0.50'):
            atual = Decimal('0.10')
        elif atual == Decimal('0.10'):
            atual = Decimal('0.05')
        elif atual == Decimal('0.05'):
            atual = Decimal('0.02')
        elif atual == Decimal('0.02'):
            atual = Decimal('0.01')
        cedulas_moedas = 0