data = input("Que dia é hoje? ")
alunos = []
chamada = []
qtd_alunos = int(input("Quantos alunos tem na sala? "))
for i in range(qtd_alunos):
    aluno_add = input()
    alunos.append(aluno_add)
alunos.sort()

for i in range(len(alunos)):
    presen = input(f"O aluno {alunos[i]} está presente? ").lower()
    if presen == "sim":
        chamada.append("Presente")
    else: chamada.append("Faltou")

print(f"\nLista Chamada ({data})")
print("Aluno | Presença\n")
t = 0
while t < len(alunos):
    print(f"{alunos[t]} | {chamada[t]}")
    t += 1

