a = int(input())
b = list(map(int,input().split()))
b_1,b_2 = b[0],b[0]
c = 0
for i in range(1,a):
    if b_2 >= b[i]:
        b_1 = b[i]
        b_2 = b[i]
    else:
        b_2 = b[i]
    c = max(c,b_2-b_1)
print(c)