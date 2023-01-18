t=int(input())
for i in range(t):
    a,b= map(str,input().split())
    c=int(a)
    for j in range(len(b)):
        print(b[j]*c,end="")
    print()