numero = int(input("Digite um número: "))
original = numero
invertido = 0

while numero > 0:
    ultimo_digito = numero % 10
    invertido = invertido * 10 + ultimo_digito
    numero = numero // 10

if original == invertido:
    print("É palíndromo")
else:
    print("Não é palíndromo")