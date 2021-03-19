import sys
sys.setrecursionlimit(50000)
def dfs(a,b):
    arr[a][b]=0
    for i in range(4):
        x = dx[i]+b
        y = dy[i]+a
        if 0 <= x < m and 0 <= y < n and arr[y][x]==1:
            dfs(y,x)

t = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(t):
    m,n,k = map(int,input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        arr[b][a] = 1
    cnt =0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt+=1
                dfs(i,j)
    print(cnt)