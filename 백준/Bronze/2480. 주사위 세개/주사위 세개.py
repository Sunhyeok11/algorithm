a,b,c = map(int,input().split())

if a==b and b==c :
    print(10000+1000*a)
elif a==b:
    print(1000+100*a)
elif b==c or c==a :
    print(1000+100*c)
else :
    print(100*max(a,b,c))