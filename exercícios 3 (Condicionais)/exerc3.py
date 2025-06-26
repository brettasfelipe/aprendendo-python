ano = input("Insira um ano: ")
ano = int(ano)
if ano % 4 == 0 and ano % 100 != 0:
    print("O ano é bissexto")
elif ano % 400 == 0:
    print("O ano é bissexto")
else: 
    print("O ano não é bissexto")