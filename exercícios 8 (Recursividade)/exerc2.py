"""
No treinamento do departamento de bombas da polícia, é preciso ser rápido para desarmar a bomba antes que ela exploda. 
Todos os policiais do setor possuem um tempo recorde em que eles conseguem desarmar a bomba, além disso cada bomba conta 
com um relógio regressivo que realiza a contagem de tempo que falta para a explosão. Porém, o programador do setor 
decidiu instalar travas de segurança nas bombas. De maneira que se o tempo recorde que o policial leva para desarmar 
uma bomba for maior que o tempo em que ela explode, a bomba é desativada automaticamente no último segundo antes de 
explodir. Caso o tempo recorde seja menor, o relógio segue com a contagem regressiva normalmente e portanto a bomba 
explode.

Implemente um programa que simule um relógio regressivo e a cada segundo informe quanto tempo falta com a frase 
“ Atenção faltam n segundos...”. Faltando apenas 5 segundos ele deve mostrar a mensagem: 
“Seu tempo está acabando”, no último segundo, caso a bomba seja desativada a frase a ser apresentada é 
“Bomba desativada automaticamente!” e se encerra a contagem regressiva, se não apresenta a frase 
“Seja rápido. Falta apenas 1 segundo” e antes de explodir, no segundo 0,  a frase “Cabum!! Explodiu”.
"""

N = int(input())
P = int(input())
n = N

def bombDefuse(N, P, n):
    if (P < N and n == 0) or N == 0: # Caso base 1
        return print("Cabum!!!! Explodiu")
    elif P >= N and n == 0: # Caso base 2
        return print("Bomba desativada automaticamente!")
    elif n == 5:
        print("Seu tempo está acabando!")
    elif n == 1 and P < N:
        print("Seja rápido. Falta 1 segundo")
    else:
        if n != 1:
            print(f"Atenção faltam {n} segundos...")
    return bombDefuse(N, P, n-1) # Chama a própria função e se aproxima do caso base

bombDefuse(N, P, n)
