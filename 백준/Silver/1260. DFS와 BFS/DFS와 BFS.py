n,m,v = map(int,input().split())

matrix=[[0]*(n+1) for _ in range(n+1) ]

visited = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for j in range(1,n+1):
        if(visited[j]==0 and matrix[v][j]==1):
            dfs(j)
def bfs(v):
    queue = [v]
    visited[v] = 0
    
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for k in range(1,n+1):
            if (visited[k]==1 and matrix[v][k]==1):
                queue.append(k)
                visited[k] = 0

dfs(v)
print()
bfs(v)