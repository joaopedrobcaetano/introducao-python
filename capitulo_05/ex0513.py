divida = float(input("Qual o valor da dívida? R$"))
taxa = float(input("Qual a taxa de juros? "))
pagamento = float(input("Qual o valor do pagamento mensal? R$"))
mes = 1
if divida * (taxa / 100) > pagamento:
    print("O valor do pagamento mensal é insuficiente para cobrir os juros.")
else:
    saldo = divida
    juros_pagos = 0
    while saldo > pagamento:
        juros = saldo * (taxa / 100)
        saldo = saldo + juros - pagamento
        juros_pagos = juros_pagos + juros
        print(f"Mês {mes}: Saldo devedor: R${saldo:.2f}")
        mes = mes + 1
    print(f"Para pagar uma dívida de R${divida:.2f} com uma taxa de juros de {taxa}% ao mês, você levará {mes - 1} meses, pagando um total de R${juros_pagos:.2f} em juros.")
    print(f"No último mês, você teria um saldo residual de R${saldo:.2f}.")