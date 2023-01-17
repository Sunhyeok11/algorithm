a=int(input())
e= 1
c = a
while True:
    q = (a//10)  + (a%10)
    a = (a%10)*10 + (q%10)
    if c == a:
        break
    else:
        e+=1
print(e)

          