a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))
e = list(map(int,input().split()))
f = []
f.append(int(sum(a)))
f.append(int(sum(b)))
f.append(int(sum(c)))
f.append(int(sum(d)))
f.append(int(sum(e)))
t= f.index(max(f))+1
print(t,max(f))