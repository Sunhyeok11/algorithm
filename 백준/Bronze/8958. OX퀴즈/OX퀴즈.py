a = int(input())

for i in range(a):
    c=0
    d=0
    b = list(input())
    for j in range(len(b)):
        if b[j] == 'O':
            c+=1
            d+=c
        else:
            c=0

    print(d)