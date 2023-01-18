a = list(map(int,input().split()))
b = [1, 2, 3, 4, 5]

while a != b:
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            print(" ".join(map(str, a)))