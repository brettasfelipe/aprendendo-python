mat1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],]

mat2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],]

res = []
list_term1 = []
list_term2 = []
b = 0
m = 4
for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        list_term1.append(mat1[i][j])
    for l in range(len(mat2[j])):
        list_term2.append(mat2[l][i])
    list_res1 = list_term1[b:m]
    list_res2 = list_term2[b:m]

    print(list_res1)
    print(list_res2)
    b += 3
    m += 3
    


    
