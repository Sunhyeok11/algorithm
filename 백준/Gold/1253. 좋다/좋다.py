import sys
input = sys.stdin.readline
N = int(input())
Result = 0 
A = list(map(int,input().split()))
A.sort()

for K in range(N):
    find = A[K]
    i = 0
    j = N - 1
    while i < j:
        if A[i] + A[j] == find:
            if i != K and j != K:
                Result  += 1
                break
            elif i == K:
                i += 1
            elif j == K:
                j -= 1
        elif  A[i] + A[j] < find:
            i += 1
        else:
            j -= 1
print(Result)