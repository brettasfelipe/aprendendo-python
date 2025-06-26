"""
Critérios senha:
    > Ela deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um caractere numérico;
    > Ela não pode ter nenhum caractere de pontuação, acentuação ou espaço;
    > Ela pode ter entre 6 e 32 caracteres (inclusivo).
"""

senha = input()
def var_carac(senha): #Função que faz a verificação dos caracteres (Maiúsculo, minúsculo, número)
    pts = 0
    tmsUP = 0 
    tmsLW = 0
    tmsNUM = 0
    for i in senha:
        if i.isupper() and tmsUP == 0: #Verificação do caracter - Maiúsculo (Feita uma única vez)
            pts += 1
            tmsUP = 1
        elif i.islower() and tmsLW == 0: #Verificação do caracter - Minúsculo (Feita uma única vez)
            pts += 1
            tmsLW = 1 
        if i.isdigit() and tmsNUM == 0: #Verificação do caracter - Número (Feita uma única vez)
            pts += 1
            tmsNUM = 1
    
    if pts >= 3: #Verificação se contém todos os requisitos
        return True
    else:
        return False

def var_alphanum(senha): #Função para verificar a existência de caracteres de acentuação, pontuação e espaços (proibidos)
    for i in senha:
        if ((not i.isalpha() and not i.isdigit()) or (i.isspace()) or (ord(i) in range(192, 256)) or (ord(i) in range(256, 383))): 
            return False
    return True

def var_numchr(senha): #Função que verifica o número de caracteres da senha
    if len(senha) in range(6, 33):
        return True
    else:
        return False
    
if var_alphanum(senha) and var_carac(senha) and var_numchr(senha): #Verificação se todos as funções são verdadeiras, e portanto, se a senha está nos conformes.
    print("Senha valida.")
else:
    print("Senha invalida.")
