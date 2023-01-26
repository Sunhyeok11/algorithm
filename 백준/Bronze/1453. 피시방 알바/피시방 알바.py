a = int(input())
b= list(map(int,input().split()))
c = [0]*101
d= 0
for i in b:
    if c[i] != 0:
        d +=1
    else:
        c[i] +=1
print(d)