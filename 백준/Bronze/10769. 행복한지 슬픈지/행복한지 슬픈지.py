a = (input())

b= [ ':-)',':-(' ]
c=0
d=0
for i in a:
    if i in b[0]:
        c+=1
    if i in b[1]:
        d+=1

if c<3 and d<3:
    print('none')
elif c>d:
    print('happy')
elif c<d:
    print('sad') 
elif c == d :
    print('unsure') 