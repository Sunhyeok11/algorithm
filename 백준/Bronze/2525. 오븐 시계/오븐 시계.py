a,b = map(int,input().split())
c=int(input())
d=b+c
e=d
n=d//60
while True:
    if d>=60*n:
        e-=60*n
        a+=1*n
        if a>=24:
            a=a-24
        break
    elif d<60:
        break
print(a ,e,sep=' ')
