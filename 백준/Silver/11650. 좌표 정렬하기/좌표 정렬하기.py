a = int(input())
b = []
for _ in range(a):
    c = list(map(int,input().split()))
    b.append(c)
b.sort()
for i in b:
    print(i[0],i[1])