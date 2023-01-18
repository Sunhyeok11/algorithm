word = input()
cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = len(word)
for i in cr:
    if i in word:
        n -= word.count(i)

print(n)