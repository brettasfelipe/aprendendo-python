catalogo = {}
lista_prod = input().split()
for i in range(0, len(lista_prod) - 1, 2):
    catalogo[lista_prod[i]] = float(lista_prod[i+1])
    
carrinho = input().split()
preco = 0 
i = 0
for item in carrinho:
    if item in catalogo:
        preco += catalogo[item] * int(carrinho[i+1])
    i += 1

print(f"R$ {preco:.2f}")
