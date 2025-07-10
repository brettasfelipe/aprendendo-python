"""
Implemente uma função recursiva chamada substituir_vogais(texto, nova_vogal) que substitui todas as vogais do texto por uma nova vogal fornecida, sem utilizar laços (for ou while).
"""

import unicodedata as uni

def substituir_vogais(texto, nova_vogal, inic=0): # Cria a função com os parâmetros pedidos e um auxiliar
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogais_upper = ['A', 'E', 'I', 'O', 'U'] # Define as vogais, tanto maiúsculas quanto minúsculas

    texto = uni.normalize('NFD', texto) # Padroniza o texto em relação aos acentos

    if inic == len(texto) - 1: # Caso base e condições específicas
        if texto[inic] in vogais: 
            return nova_vogal
        
        elif texto[inic] in vogais_upper: # Caso a vogal a ser substituída seja maiúscula, a nova também deve ser
            return nova_vogal.upper()
        
        else: 
            return texto[inic] # Se for consoante, retorna a consoante 
        
    else: # Os 3 próximos casos seguem o mesmo princípio dos de cima, para quando não é aplicado o caso base. 
        if texto[inic] in vogais:
            return nova_vogal + substituir_vogais(texto, nova_vogal, inic+1)
        
        elif texto[inic] in vogais_upper:
            return nova_vogal.upper() + substituir_vogais(texto, nova_vogal, inic+1)
        
        else:
            return texto[inic] + substituir_vogais(texto, nova_vogal, inic+1)
        # Nos 3 casos a função é chamada novamente e ocorre a aproximação do caso base
