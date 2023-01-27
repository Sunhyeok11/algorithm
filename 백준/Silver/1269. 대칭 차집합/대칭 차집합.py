len_a,len_b = map(int,input().split())

a= input().split()
b= input().split()
a = set(a)
b = set(b)

print(len(a^b))