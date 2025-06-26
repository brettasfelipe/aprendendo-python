import random as rd

numBola = 0
maiorBola = -10**6 - 1
menorBola = 10**6 + 1
while numBola < 1000:
    novaBola = rd.randint(-10**6, 10**6)
    if novaBola > maiorBola:
        maiorBola = novaBola
    if novaBola < menorBola:
        menorBola = novaBola
    numBola += 1
    print(f"A urna está com {numBola} bolas. A última bola foi {novaBola}!")

print("O maior número na urna é: ", maiorBola)
print("O menor número na urna é: ", menorBola)

# .append => serve pra adicionar um item a uma lista criada anteriormente
# max() mostra o maior número da lista
# min() mostra o menor número da lista
# len() conta o num de algarismos em uma lista, por exemplo (da pra usar em outros contextos)