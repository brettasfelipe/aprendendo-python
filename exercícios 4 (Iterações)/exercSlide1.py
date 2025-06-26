num = int(input())
soma = 0
if num%2 == 0:
    print("O número não é ímpar")
else:
    for i in range(1, num+1, 2):
        soma += i
    print(soma)