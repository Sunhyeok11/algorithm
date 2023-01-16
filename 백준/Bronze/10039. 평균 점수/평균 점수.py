a =int(input())
b =int(input())
c =int(input())
d =int(input())
e =int(input())
w= 0
r=0
t=0
y=0
u=0

if a %5 == 0:
    w += a
    if a <40:
        w += 40 -a
if b %5 == 0:
    r += b
    if b <40:
        r += 40 -b
if c %5 == 0:
    t += c
    if c <40:
        t += 40-c
if d %5 == 0:
    y += d
    if d <40:
        y += 40-d
if e %5 == 0:
    u += e
    if e <40:
        u += 40-e
q = (w+r+t+y+u)//5

print(q)