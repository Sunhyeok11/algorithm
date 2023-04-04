import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    c = input().split()

    if len(c) == 1:
        c0 = c[0]
    else:
        c0,c1 = c

    if c0 == "add":
        S.add(int(c1))

    elif c0 == "remove":
        if int(c1) in S:
            S.remove(int(c1))

    elif c0 == "check":
        if int(c1) in S:
            print(1)
        else:
            print(0)

    elif c0 == "toggle":
        if int(c1) in S:
            S.remove(int(c1))
        else:
            S.add(int(c1))

    elif c0 == "all":
        S = {1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20}

    else:
        S.clear()