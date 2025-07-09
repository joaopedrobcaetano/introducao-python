salario = float(input('Digite o salário do funcionário: '))
aumento = float(input('Digite a porcentagem de aumento: '))
novo_salario = salario + (salario * aumento / 100)
print(f"O funcionário recebeu um aumento de R$ {(novo_salario - salario):.2f} e seu novo salário é: R$ {novo_salario:.2f}")