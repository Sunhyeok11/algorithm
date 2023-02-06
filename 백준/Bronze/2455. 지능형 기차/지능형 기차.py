b=[]
c=0
max_c =0
for i in range(4):
    a= list(map(int,input().split()))
    b.append(a)
for j in range(4):
    c+=b[j][1]-b[j][0]
    if c>max_c:
        max_c =c
print(max_c)