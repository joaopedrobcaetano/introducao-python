n = int(input("Quantos números primos você quer ver? "))
contador = 0
num_atual = 2

while contador < n:
    eh_primo = True

    if num_atual == 2:
        eh_primo = True
    elif num_atual % 2 == 0:
        eh_primo = False
    else:
        i = 3
        limite = int(num_atual ** (1/2)) + 1
        while i <= limite:
            if num_atual % i == 0:
                eh_primo = False
                break
            i += 2

    if eh_primo:
        print(num_atual, end=' ')
        contador += 1

    num_atual += 1