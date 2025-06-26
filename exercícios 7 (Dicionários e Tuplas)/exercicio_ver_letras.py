frase = input()
term = {
    "d": 0,
    "t": 0,
    "v": 0
}
for letra in frase:
    if letra == "d":
        term["d"] += 1
    elif letra == "t":
        term["t"] += 1
    elif letra == "v":
        term["v"] += 1

for chave, valor in term.items():
    if valor != 0:
        print(chave, valor)