"""
Implemente uma função chamada invert_dict que tem como argumento um dicionário d e que retorne um dicionário invertido - onde a chave deve ser o valor e o valor uma lista das chaves. A lista de chaves deve manter a ordem original do dicionário.
"""

def invert_dict(d):
    # Cria um novo dicionário que será a lista final (invertida)
    new_dict = {}

    # Itera cada par chave, valor, do dicionário base
    for key, value in d.items():

        # Verifica se a chave(valor) já não foi adicionada, caso ele não esteja no novo dicionario, cria uma lista com esse valor(chave)
        if value not in new_dict:
            new_dict[value] = [key]

        # Caso a chave(valor) já esteja no dicionário, apenas coloca o valor da chave repetida na lista
        else: 
            new_dict[value].append(key)
    return new_dict

# Outra maneira de fazer: (Uso do método setdefault()):

def invert_dict_setdefault(d):
    new_dict = {}
    for key, value in d.items():    
        new_dict.setdefault(value, []).append(key)
    return new_dict

d = dict(antonio=10, maria=10, pedro=9.5, joao=10, tereza=9, ana=9)
print(invert_dict_setdefault(d))