"""
Julie gosta de registrar seus hábitos, e agora ela tem um novo: seguindo a orientação de sua nutricionista, ela precisa tomar um pequeno comprimido de vitamina b todos os dias. Como ela quer acompanhar esse hábito e ver todos os dias quantos comprimidos restam no pote e quantos ela já consumiu, escreva uma função recursiva controle(n,c), que a cada dia mostra um aviso "Voce ja tomou c comprimidos, restam _.", e no caso de ser o último exiba a mensagem "Parabens Julie! Voce tomou todos os n comprimidos!", onde n é o número de comprimidos que tem em um pote cheio e c é a quantidade já consumida por Julie (na primeira chamada da função, c é necessariamente 0). 
"""

def controle(n, c):
    if n == 0: # Caso base
        return print(f"Parabens Julie! Voce tomou todos os {c} comprimidos!")
    elif c == 0:
        return controle(n-1, c+1)
    else:
        print(f"Voce ja tomou {c} comprimidos, restam {n}.")
        return controle(n-1, c+1) # Aproximação do caso base e chamada da função

