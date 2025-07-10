"""
Jurandir quer montar um painel de LEDs contendo diversas letras e números para seu Pet Shop. Ele não possui muitos LEDs, e não tem certeza se conseguirá montar a cadeia de caracteres desejada. Considerando a configuração do alfabeto eletrônico em LEDs das letras e números abaixo, faça um algoritmo que ajude Jurandir a descobrir a quantidade de LEDs necessários para montar uma frase.

No exercício original possuía uma imagem na qual aparecia o número de leds necessário pra cada digito.
"""

# Criação de um dicionário com o "n° de leds" que cada dígito precisa
dic_leds = {
    "a": 8, "b": 10, "c": 6, "d": 8, "e": 7, "f": 5, "g": 8, "h": 6, "i": 6, "j": 5, "k": 5, "l": 4, "m": 6, "n": 6, "o": 8, "p": 7, "q": 9, "r": 8, "s": 8, "t": 4, "u": 6, "v": 4, "w": 6, "x": 4, "y": 3, "z": 6, 

    "1": 3, "2": 8, "3": 7, "4": 5, "5": 8, "6": 9, "7": 5, "8": 10, "9": 9, "0": 8      
}

# Pede um input colocando todos as letras minúsculas, pois o dicionário foi estabelecido em minúsculas
palavra = input().lower()
soma = 0
for i in palavra:

    # Verifica se o termo iterado é um espaço, se for, ignora, pois não usa leds
    if i == " ":
        pass

    # Se for um termo diferente do espaço, soma o valor desse dígito
    else:
        soma += dic_leds[i]

print(f"{soma} LEDs")