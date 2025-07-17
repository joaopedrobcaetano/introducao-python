deposito_inicial = float(input("Qual o valor do depósito inicial? R$"))
taxa_juros = float(input("Qual o valor da taxa de juros? "))
total_acumulado = deposito_inicial
mes = 1
while mes <= 24:
    total_acumulado = total_acumulado + (total_acumulado * taxa_juros / 100)
    print(f"Após o mês {mes}, o total acumulado é R${total_acumulado:.2f}")
    mes = mes + 1
print(f"O rendimento total foi de R${total_acumulado - deposito_inicial:.2f}")