n = int(input())
c=[]
for i in range(1,n+1):
    s = i + sum(list(map(int,str(i))))
    if(s==n):
        c.append(i)
if c == []:
    print(0)
elif c != []:
    print(min(c))