a=0
b=[0]*1001
for _ in range(10):
    c = int(input())
    a+=c
    b[c] +=1
print(a//10)
print(b.index(max(b)))