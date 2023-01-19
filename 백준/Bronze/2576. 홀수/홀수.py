a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())

t=[]
if a%2 ==1:
    t.append(a)
if b%2 ==1:
    t.append(b)
if c %2 ==1:
    t.append(c)
if d %2 ==1:
    t.append(d)
if e %2 ==1:
    t.append(e)
if f %2 ==1:
    t.append(f)
if g %2 ==1:
    t.append(g)

if  t != []:
    t.sort()
    print(sum(t))
    print(t[0])
if t == []:
    print(-1)
