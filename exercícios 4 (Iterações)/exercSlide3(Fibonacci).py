num = int(input())
n1 = 0
n2 = 1
if num <= 1:
    print(num)
else:
    for i in range(2, num+1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")


    
     
    
