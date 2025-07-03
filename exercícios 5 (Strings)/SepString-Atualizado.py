"""
Johnny é um cara legal que gostava de carros e brincar com algoritmos de compressão. Ele está trabalhando em um projeto no qual tem que lidar com cadeias de caracteres extremamente grandes. O maior problema de Johnny nesse trabalho é que essas strings são grandes demais para manipular diretamente, então ele precisa de uma representação alternativa (menor) para a mesma informação. Johnny pensou em usar uma técnica bem conhecida para comprimir as strings: trocar ocorrências consecutivas de um mesmo caractere por uma única ocorrência deste mesmo caractere, seguida da quantidade de ocorrências. Neste formato, todo caractere é seguido por um inteiro positivo. Essa compressão permitiu que ele comunicasse suas strings, mas ele não consegue processá-las corretamente e agora precisa da sua ajuda para revertê-las às suas formas originais.
"""

n =  int(input())
letra = ""
num = "0"

for _ in range(n):
    string = input()
    
    for j in range(len(string)):
        # Condição de Parada
        if (not string[j].isnumeric()) and j > 0:
            print(letra*int(num), end="")
            num = "0"
        # Armazenar um valor não numérico
        if not string[j].isnumeric():
            letra =  string[j]
        # Armazenar valor numérico
        else:
            num = num + string[j]

    # Print final
    print(letra*int(num))
    num = "0"