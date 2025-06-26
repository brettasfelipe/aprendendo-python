num = int(input())
for i in range(num):
    cod = input()
    digit = ""
    vez = "0"
    t = 0
    while True:
        if ((cod[t].isnumeric() == False) and (digit != cod[t])) and t > 0:
            print(digit*int(vez), end="")
            vez = "0"
            digit = ""
        if cod[t].isnumeric() == False:
            digit = cod[t]
            t += 1
        else:
            vez = str(vez) + cod[t]
            t += 1        
        
        if len(cod) == t:
            print(digit*int(vez))
            break


        


