N, M = map(int,input().split())
a = list(map(int, input().split()))
b = 0
for i in range (0,N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            c = a[i] + a[j] + a[k]
            if c > b and c <= M:
                b = c            

print(b)