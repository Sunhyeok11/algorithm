c=[]
d=[]
for i in range(3):
    a,b = (map(int,input().split()))
    c.append(a)
    d.append(b)
    c.sort()
    d.sort()

if c[0] == c[1]:
    if d[0] == d[1]:
        print(f'{c[2]} {d[2]}')
    else:
        print(f'{c[2]} {d[0]}')
else:
    if d[0] == d[1]:
        print(f'{c[0]} {d[2]}')
    else:
        print(f'{c[0]} {d[0]}')