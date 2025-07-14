numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (soma, subtração, multiplicação ou divisão): ")
if operacao == "soma":
    resultado = numero_1 + numero_2
elif operacao == "subtração":
    resultado = numero_1 - numero_2
elif operacao == "multiplicação":
    resultado = numero_1 * numero_2
elif operacao == "divisão":
    if numero_2 == 0:
        resultado = "Erro: Divisão por zero"
    else:
        resultado = numero_1 / numero_2
else:
    resultado = "Operação inválida"
print(f"O resultado da {operacao} é: {resultado}")