num = int(input())
i = 1
div = 0
while i < num:
    if num%i == 0:
        div += i
        if div == num:
            print(i, end=" ")
