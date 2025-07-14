valor_da_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: "))
prestacao_maxima = float(salario * 0.3)
anos_a_pagar = int(input("Digite em quantos anos deseja pagar: "))
prestacao_mensal = valor_da_casa / (anos_a_pagar * 12)
if prestacao_mensal > salario * 0.3:
    print(f"Empréstimo negado: a prestação mensal excede 30% do salário, que é R${prestacao_maxima:.2f}.")
else:
    print(f"Empréstimo aprovado: você irá pagar {anos_a_pagar * 12} parcelas de R${prestacao_mensal:.2f}.")