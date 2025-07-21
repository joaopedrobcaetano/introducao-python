numero = int(input("Digite um número para verificar se ele é primo: "))
if numero <= 1:
    print("Não é primo.")
elif numero == 2:
    print("É primo.")
elif numero % 2 == 0:
    print("Não é primo.")
else:
    i = 3
    limite = int(numero ** (1/2)) + 1
    eh_primo = True

    while i <= limite:
        if numero % i == 0:
            eh_primo = False
            break
        i += 2

    if eh_primo:
        print("É primo.")
    else:
        print("Não é primo.")