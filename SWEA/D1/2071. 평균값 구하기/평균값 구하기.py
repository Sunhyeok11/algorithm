t= int(input())

for i in range(1,t + 1):
    a = list(map(int,input().split()))
    w = len(a)
    q = sum(a)
    p = q / w

    print(f'#{i} {round(p)}')