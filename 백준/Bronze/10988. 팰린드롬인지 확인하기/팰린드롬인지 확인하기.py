a=str(input())
c=0
d=len(a)//2
for i in range(len(a)):
    if a[i] == a[-i-1]:
        c+=1
    else:
        c+=0
if c>d:
    print(1)
else:
    print(0)