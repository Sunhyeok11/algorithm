a = int(input())

for i in range(a):
    b = []
    c=input()
    for j in c:
        if j == '(':
            b.append(j)
        elif j == ')':
            if b:
                b.pop()
            else: 
                print("NO")
                break
    else: 
        if not b:
            print("YES")
        else: 
            print("NO")