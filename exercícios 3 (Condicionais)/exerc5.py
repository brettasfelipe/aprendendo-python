diaInc = int(input("Insira o dia em que o show irá começar: "))
horInc, minInc, segInc = map(int, input("Insira o horário que o show começará: (h:m:s): ").split(":"))
diaFin = int(input("Insira o dia em que o show irá terminar: "))
horFin, minFin, segFin = map(int, input("Insira o horário que o show terminará: (h:m:s): ").split(":"))
 
duracao = (diaFin-diaInc)*86400 + (horFin-horInc)*3600 + (minFin-minInc)*60 + (segFin-segInc)

if duracao < 0:
    print("A data inserida é inválida")
else:
    totDias = duracao//86400
    totHoras = (duracao%86400)//3600
    totMin = ((duracao%86400)%3600)//60
    totSeg = ((duracao%86400)%3600)%60
    
    print(f"{totDias} dia(s)\n{totHoras} hora(s)\n{totMin} minuto(s)\n{totSeg} segundo(s)")
