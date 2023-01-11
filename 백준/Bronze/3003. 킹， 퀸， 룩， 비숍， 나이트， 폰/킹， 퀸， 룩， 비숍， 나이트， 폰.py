k, q, l, b, n, p = map(int, input().split())

chess = [k, q, l, b, n, p]

chess_rull = [1, 1, 2, 2, 2, 8]

for i in range(len(chess)):

    chess[i] = chess_rull[i] - chess[i]

print(*chess)