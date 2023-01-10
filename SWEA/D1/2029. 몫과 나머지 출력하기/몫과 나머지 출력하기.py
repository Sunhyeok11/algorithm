t= int(input())

for i in range(1,t + 1):
    a,b = list(map(int,input().split())) 

    q = a // b
    w = a % b
    print(f"#{i} {q} {w}")

