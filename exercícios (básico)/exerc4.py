"""
valor = input("Insira True ou False: ")
if valor == "True":
    print("False")
elif valor == "False":
    print("True")
else: print("Valor inválido")
"""   

valor = bool(int(input("Insira algum valor para True, deixe em branco para False: ")))
print(bool(not valor))