a = int(input())
r=[]
for i in range(a):
    b = input().split()
    for j in b:
        t = list(j)
        t.reverse()
        print("".join(t),end=' ')
    print()