preco_mercadoria = float(input('Digite o preço da mercadoria: '))
desconto = float(input('Digite a porcentagem de desconto: '))
preco_final = preco_mercadoria - (preco_mercadoria * desconto / 100)
print(f"O desconto foi de R$ {(preco_mercadoria - preco_final):.2f} e o preço final da mercadoria é: R$ {preco_final:.2f}")