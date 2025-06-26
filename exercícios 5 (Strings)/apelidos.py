name = input()
def eh_composto(name):
    for i in name:
        if i == " ":
            return True
    return False

if eh_composto(name):
    indc = name.find(" ")
    comp = name[indc+1:indc+3]
    apel = name[0:2] + comp
    print(apel)
elif len(name) == 3:
    apel = name[0:2]
    print(apel)
elif len(name) > 3:
    apel = name[0:3]
    print(apel)
else:
    apel = name
    print(apel)
