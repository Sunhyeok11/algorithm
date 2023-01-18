a = input()

if len(a) <= 10:
    print(a)

else:
    for i in range(len(a)//10+1):
        print(a[i*10:(i+1)*10])
