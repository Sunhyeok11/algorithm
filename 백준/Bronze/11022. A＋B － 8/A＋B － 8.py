a=int(input())

for i in range(1,a+1):
    a,b=map(int,input().split())
    c = a+b
    print(f'Case #{i}: {a} + {b} = {c}')