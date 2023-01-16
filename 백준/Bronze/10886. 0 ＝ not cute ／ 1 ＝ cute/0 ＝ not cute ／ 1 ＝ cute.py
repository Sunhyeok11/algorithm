N = int(input())
b = 0

if N % 2 ==1:
    for i in range(1,N+1):
        a = int(input())
        if a ==1:
            b+=1
    if b/N <0.5:
        print("Junhee is not cute!")
    else:
        print("Junhee is cute!")