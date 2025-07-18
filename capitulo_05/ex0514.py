soma = 0
quantidade_numeros = 0
while True:
    n = int(input("Digite um número para somar ou 0 para terminar a soma: "))
    if n == 0:
        break
    soma += n
    quantidade_numeros += 1
print(f"A soma dos números digitados é {soma}.")
print(f"A média é {(soma / quantidade_numeros):.2f}.")