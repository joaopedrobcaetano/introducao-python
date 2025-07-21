n = float(input("Digite um número para calcular a raiz quadrada: "))

b = 2.0
p = (b + (n / b)) / 2

while abs(n - p * p) >= 0.0001:
    b = p
    p = (b + (n / b)) / 2

print("A raiz quadrada aproximada de", n, "é", p)