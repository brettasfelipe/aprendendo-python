n =  int(input())
corredores = []
for _ in range(n):
    items =  corredores.append(input().split())

e = int(input())
if e > n:
    print("Esse corredor não existe no mercado.")
else:    
    catalogo_cord = {}
    for i in range(0, len(corredores[e-1]) - 1, 2):
        catalogo_cord[corredores[e-1][i]] = float(corredores[e-1][i+1])
    items = list(catalogo_cord)
    prec_medio = sum(catalogo_cord.values())/len(catalogo_cord)
    
    print(f"No corredor {e} encontramos:")
    print(*items, sep=", ")
    print(f"E o preço médio é {prec_medio:.2f}.")