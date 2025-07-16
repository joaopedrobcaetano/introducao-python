dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
resultado = 0
contador = 1
while divisor <= dividendo:
    dividendo = dividendo - divisor
    resultado = resultado + 1
    contador = contador + 1
print(f"Resultado: {resultado} (Resto: {dividendo})")