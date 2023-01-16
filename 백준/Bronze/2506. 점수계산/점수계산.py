a = int(input())
b = list(map(int,input().split()))
c = 0
q = 0
for i in range(a):
    if b[i] ==1:
        c +=1
        q +=c
    else:
        c = 0
print(q)