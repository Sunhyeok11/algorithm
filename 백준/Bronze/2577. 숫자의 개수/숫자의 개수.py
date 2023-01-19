a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)

e = {'0': 0, '1': 0,'2':0,'3': 0, '4': 0,'5':0,'6': 0, 
'7': 0,'8':0,'9': 0}

for i in d:
    if i in e:
        e[i] +=1
for j in e.values():
    print(j)