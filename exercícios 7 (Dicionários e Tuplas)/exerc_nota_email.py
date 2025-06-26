def aprovado(d):
    nf = (sum(d[nom_email][1:]))/4
    if nf >= 5:
        return "aprovado", nf
    else: 
        return "reprovado", nf

n = int(input())
quadro_info = {}
for _ in range(n):
    nome, email, n1, n2, n3, n4 = input().split()
    quadro_info[nome] = [email, float(n1), float(n2), float(n3), float(n4)]

nom_email = input()

if nom_email not in quadro_info:
    print(f"O aluno {nom_email} não está na turma.")
else:
    aprov, nf = aprovado(quadro_info)
    print(f"Destinatário: {quadro_info[nom_email][0]}\nO aluno {nom_email} foi {aprov} com média {nf:.2f}.")