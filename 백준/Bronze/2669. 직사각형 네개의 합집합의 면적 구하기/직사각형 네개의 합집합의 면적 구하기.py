matrix = []
for _ in range(100):
    matrix.append([0]*100)
c = 0
for i in range(4):
    a, b, x, y = map(int, input().split())
    for j in range(a, x): 
        for k in range(b, y):
            if matrix[j][k] == 0:
                matrix[j][k] += 1
                c += 1
print(c)