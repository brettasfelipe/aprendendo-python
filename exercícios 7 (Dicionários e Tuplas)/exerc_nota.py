
n = int(input())
plan_notas = {}
for _ in range(n):
    nome, nota = input().split(", ")
    plan_notas[nome] = float(nota)

nota = float(input())
nome_igual = [key for key, value in plan_notas.items() if value == nota]
nome_igual = sorted(nome_igual)

if nome_igual:
    print(*nome_igual, sep="/")
else: 
    print("Você foi o único aluno com essa nota.")
