a = int(input())

g = [1,2,3]

for i in range(1,a+1):
    b,c = map(int,input().split())

    g[b-1],g[c-1] = g[c-1],g[b-1]

print(g.index(1)+1)