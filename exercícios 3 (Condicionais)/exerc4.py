def biss(ano):
    ano = int(ano)
    if ano % 4 == 0 and ano % 100 != 0:
        return "bissexto"
    elif ano % 400 == 0:
        return "bissexto"
    else: 
        return "não bissexto"


dia, mês, ano = map(int, input("Insira sua data de nascimento no format dia/mês/ano: ").split(sep="/"))
if mês > 12 or mês < 1 or ano < 0:
    print("Data inválida")
elif mês == 1 or mês == 3 or mês == 5 or mês == 7 or mês == 8 or mês == 10 or mês == 12 and dia <= 31:    
    print("Data válida")
elif mês == 4 or mês == 6 or mês == 9 or mês == 11 and dia <= 30:  
    print("Data válida")
elif mês == 2 and dia <= 28:
    print("Data válida")
elif mês == 2 and biss(ano) == "bissexto" and dia <= 29:
    print("Data válida")
else:
    print("Data inválida")