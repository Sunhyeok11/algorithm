d = []
a= list(map(int,input().split()))
b= list(map(int,input().split()))
c= list(map(int,input().split()))
a_1 = d.append(sum(a))
b_1 = d.append(sum(b))
c_1 = d.append(sum(c))
for i in d:
    if i == 1:
        print('C')
    elif i == 2:
        print('B')
    elif i == 3:
        print('A')
    elif i == 0:
        print('D')
    elif i == 4:
        print('E')