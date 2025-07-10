salario = float(input("Qual é o salário do funcionário? "))
if salario > 1250:
    aumento = salario * 0.1
    novo_salario = salario + aumento
if salario <= 1250:
    aumento = salario * 0.15
    novo_salario = salario + aumento
print(f"O funcionário recebeu um aumento de R${aumento:.2f}, e seu novo salário é R${novo_salario:.2f}.")