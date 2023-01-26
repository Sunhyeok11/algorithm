a = int(input())
c= []
for i in range(a):
    b = int(input())
    if b == 0:
        c.pop()
    else:
        c.append(b)
print(sum(c))