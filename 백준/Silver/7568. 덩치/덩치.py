a= int(input())
k=[]
m=[]
p=[1]*a

for i in range(a):
    x,y = list(map(int,input().split()))
    k.append(x)
    m.append(y)
for j in range(a):
    for t in range(a):
        if k[j]<k[t] and m[j]<m[t]:
            p[j] +=1

for k1 in p:
    print(k1,end=' ')