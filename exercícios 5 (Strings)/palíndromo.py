"""str.replace(old, new, count=-1)
Se o count for = -1 (padrão), todas as ocorrências serão substituídas"""


n = input()
x = 0
y = -1
t = 0

if (n == n[::-1]) and (len(n)%2 == 0):
    print("OFF")
else:
    while True:
        if (t == 1) or (n == n[::-1]):
            break
        else:
            if n[x] == n[y]:
                x += 1
                y += -1
            else: 
                n = n.replace(n[x], n[y], 1)
                t = 1


    if n == n[::-1]:
        print("ON")
    else: print("OFF") 
        

       