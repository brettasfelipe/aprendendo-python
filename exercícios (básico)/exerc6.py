a = int(input("Insira o coeficente a de uma equação do 2 grau: "))
b = int(input("Insira o coeficiente b de uma equação do 2 grau: "))
c = int(input("Insira o coeficiente c de uma equação do 2 grau: "))

delta = b**2 - 4*a*c 
if delta >= 0:
    bhaskara1 = (-b + delta**0.5)/2*a
    bhaskara2 = (-b - delta**0.5)/2*a 
    print(f"A primeira raiz é {bhaskara1}")
    print(f"A segunda raiz é {bhaskara2}")
else: 
    print("O delta deu negativo")

"""
delta = b**2 - 4*a*c 
bhaskara1 = (-b + delta**0.5)/2*a
bhaskara2 = (-b - delta**0.5)/2*a 
print(f"A primeira raiz é {bhaskara1}")
print(f"A segunda raiz é {bhaskara2}")
"""