a = int(input())
b = input().split()
sum = 0

for i in range(a):
    b[i] = int(b[i])
    
max_ = max(b)

for i in b:
    i = (i/max_) * 100
    sum += i

c = sum / a
print(c)