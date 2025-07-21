dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
resultado = 0
contador = 1
x = dividendo
while divisor <= x:
    x = x - divisor
    resultado = resultado + 1
    contador = contador + 1
resto = x
print(f"O resto da divisão entre {dividendo} e {divisor} é {resto}.")