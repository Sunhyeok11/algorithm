a= int(input())
c = []
for i in range(a):
    b = input()
    c.append(b)
c=set(c)
c = list(c)
c.sort()
c.sort(key=len)
for j in c:
    print(j)