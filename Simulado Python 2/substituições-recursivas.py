import unicodedata as uni

def substituir_vogais(texto, nova_vogal, inic=0):
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogais_upper = ['A', 'E', 'I', 'O', 'U']

    texto = uni.normalize('NFD', texto)
    if inic == len(texto) - 1:
        if texto[inic] in vogais: 
            return nova_vogal
        elif texto[inic] in vogais_upper:
            return nova_vogal.upper()
        else:
            return texto[inic]
    else:
        if texto[inic] in vogais:
            return nova_vogal + substituir_vogais(texto, nova_vogal, inic+1)
        elif texto[inic] in vogais_upper:
            return nova_vogal.upper() + substituir_vogais(texto, nova_vogal, inic+1)
        else:
            return texto[inic] + substituir_vogais(texto, nova_vogal, inic+1)
        
print(substituir_vogais("Olá Mundo", "e"))