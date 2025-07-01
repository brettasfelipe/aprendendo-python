"""
Amilton é um excelente corredor de fórmula 1, grande parte do seu desempenho vem da alta tecnologia em seu carro. Uma tecnologia bastante usada é o controle de desgaste dos pneus.
Em uma corrida, é de extrema importância trocar os pneus na hora certa e existem tipos de pneus diferentes que proporcionam uma quantidade diferente de voltas na pista.

Escreva a função recursiva corrida em que cada execução representa uma volta no circuito.

A função receberá três inteiros; a,b,c≥1. a representa a quantidade de voltas que faltam para a corrida acabar, b representa e quantidade de voltas que faltam para os pneus desgastarem e c representa quantas voltas os pneus suportam.
"""

def corrida(a,b,c):
    if a == 0:
        return print("A corrida chegou ao fim.") # Caso base
    elif b == 0:
        print(f"Faltam {a} voltas, hora de trocar os pneus.")
        return corrida(a-1, c-1, c) # Se aproxima do caso base e chama a função, mas "reseta" as voltas do pneu
    else:
        return corrida(a-1, b-1, c) # Se aproxima do caso base e chama a função 


    
    
    