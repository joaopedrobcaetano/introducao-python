opcao = int(input("Escolha uma opção: [1] Adição [2] Subtração [3] Divisão [4] Multiplicação [5] Sair: "))

while (opcao != 5):
    if (opcao == 1):
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} + {numero} = {tabuada + numero}")
                numero += 1
            tabuada += 1

    elif (opcao == 2):
        tabuada = 1
        while tabuada <= 10:
            numero = tabuada + 10
            while numero >= tabuada:
                print(f"{numero} - {tabuada} = {numero - tabuada}")
                numero -= 1
            tabuada += 1

    elif (opcao == 3):
        tabuada = 2
        while tabuada <= 10:
            numero = tabuada
            while numero <= tabuada * 10:
                print(f"{numero} / {tabuada} = {numero / tabuada}")
                numero += tabuada
            tabuada += 1

    elif (opcao == 4):
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} x {numero} = {tabuada * numero}")
                numero += 1
            tabuada += 1

    else:
        print("Opção inválida.")

    opcao = int(input("Escolha uma opção: [1] Adição [2] Subtração [3] Divisão [4] Multiplicação [5] Sair: "))
else:
    print("Fim do programa.")