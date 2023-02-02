b=[]
c=[]
for _ in range(20):
    a = int(input())
    if len(b)>=10:
        c.append(a)
    else:
        b.append(a)

b.sort()
c.sort()
print(sum(b[7:10]),sum(c[7:10]))