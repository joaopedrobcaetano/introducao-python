valor_a_pagar = 0
while True:
    produto = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    if produto == 1:
        valor_a_pagar = valor_a_pagar + (quantidade * 0.50)
    elif produto == 2:
        valor_a_pagar = valor_a_pagar + (quantidade * 1)
    elif produto == 3:
        valor_a_pagar = valor_a_pagar + (quantidade * 4)
    elif produto == 5:
        valor_a_pagar = valor_a_pagar + (quantidade * 7)
    elif produto == 9:
        valor_a_pagar = valor_a_pagar + (quantidade * 8)
    elif produto == 0:
        break
    else:
        print("Código inválido.")
print(f"Valor da compra: R$ {valor_a_pagar:.2f}")