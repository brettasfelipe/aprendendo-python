"""
Crie a função recursiva JaChegou que recebe dois parâmetros, sendo um inteiro n e uma cadeia de caracteres s. Enquanto n≠0 imprima a cadeia s e chame a função recursiva JaChegou com os parâmetros n-1 e s. Caso n=0, não faça nada.
"""

def JaChegou(n, s):
    if n == 0: # Caso base
        return 
    else:
        print(s)
        return JaChegou(n-1, s) # Aproxima do caso base e chama função
