a = int(input())
c = []
for i in range(1,a+1):
    d=0
    e=0
    f=0
    r=0
    b = int(input())
    c.insert(0,b//25)
    d += b%25
    c.insert(1,d//10)
    e += d%10
    c.insert(2,e//5)
    f += e%5
    c.insert(3,f//1)
    r += f%1
    print(*c)
    c.clear()