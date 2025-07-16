a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resultado = 0
contador = 1
while contador <= b:
    resultado = resultado + a
    contador = contador + 1
print(f"{a} x {b} = {resultado}")