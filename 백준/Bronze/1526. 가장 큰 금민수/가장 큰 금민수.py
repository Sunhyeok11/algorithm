a = int(input())
while True:
    b = True
    for i in str(a):
        if i!="4" and i!="7":
            b = False
            a -= 1
    if b :
        print(a)
        break