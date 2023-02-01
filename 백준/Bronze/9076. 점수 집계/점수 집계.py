a = int(input())
for i in range(a):
    b = list(map(int,input().split()))
    b.sort()
    b.pop()
    b.pop(0)
    if ( int(b[len(b)-1]) - int(b[0]) )>=4:
        print('KIN')
    else:
        print(int(sum(b)))