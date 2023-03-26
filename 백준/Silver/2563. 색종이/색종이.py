a = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(a):
    b, c = map(int, input().split())
    for i in range(b, b+10):
        for j in range(c, c+10):
            paper[i][j] = 1

answer = 0
for i in paper:
    answer += i.count(1)
print(answer)