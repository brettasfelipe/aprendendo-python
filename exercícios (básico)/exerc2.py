"""
fahrenheit = float(input("Insira uma temperatura Fahrenheit: "))
celsius =  (fahrenheit-32)*5/9
print("A temperatura em graus celsius é: ", celsius)
"""
temperatura = input("Quer transformar para Fahrenheit ou pra Celsius: ")
if temperatura == "Fahrenheit":
    temp = float(input("Insira a temperatura em Celsius: "))
    fahrenheit = 9*temp/5+32
    fahrenheit = round(fahrenheit, 2)
    print(f"A temperatura em graus Fahrenheit é: {fahrenheit}")
elif temperatura == "Celsius":
    temp = float(input("Insira a temperatura em Fahrenheit: "))
    celsius = (temp-32)*5/9
    celsius = round(celsius, 2)
    print(f"A temperatura em graus Celsius é: {celsius}")
else: print("Nomenclatura invalida.")
    