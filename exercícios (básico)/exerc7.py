"""
produto = float(input("Insira o valor do produro: "))
qtd = float(input("Insira a quantidade desse produto: "))
salario = float(input("Insira seu salário: "))

if produto*qtd <= salario:
    print(True)
else: print(False)   
"""

produto = float(input("Insira o valor do produro: "))
qtd = float(input("Insira a quantidade desse produto: "))
salario = float(input("Insira seu salário: "))
print("Você têm condições de arcar com a compra?")
print(qtd*produto<=salario)