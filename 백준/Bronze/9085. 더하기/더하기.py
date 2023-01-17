d=[]
e=0
a=int(input())
for i in range(1,a+1):
    b=int(input())
    c=list(map(int,input().split()))
    e=sum(c)
    d.append(e)
for i in range(a):
    print(d[i])