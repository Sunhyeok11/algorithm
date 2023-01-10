t= int(input())

for i in range(1,t + 1):
    a = list(map(int,input().split()))
    
    b= a.sort()
    c = a.pop()
    print(f'#{i} {c}')