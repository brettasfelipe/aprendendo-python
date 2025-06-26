n1, n2, n3 = map(int, input().split())
tipo = input()

if tipo == "P":
    print("Ponderada")
    p1, p2, p3 = map(int, input().split())
    media = (p1*n1+p2*n2+p3*n3)/(p1+p2+p3)
    print(f"{media:.2f}")
elif tipo == "H":
    print("Harmonica")
    media = 3/(1/n1+1/n2+1/n3)
    print(f"{media:.2f}")
elif tipo == "A":
    print("Aritmetica")
    media = (n1+n2+n3)/3
    print(f"{media:.2f}")
else: print("Operacao Inexistente")