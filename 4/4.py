print("for n x m matrix, enter n and m: ", end = "")
nm = input().split()
nm[0] = int(nm[0])
nm[1] = int(nm[1])

matrix = []
for i in range(nm[0]):
    t = []
    for j in range(nm[1]):
        n = int(input())
        t.append(n)
    matrix.append(t)

for i in range(len(matrix)):
    print(matrix[i])