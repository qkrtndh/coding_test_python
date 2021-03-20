from collections import deque

m,n,h = map(int,input().split())
arr =[[[] for _ in range(n)] for _ in range(h)]

dh=[1,-1,0,0,0,0]
dy = [0,0,0,0,1,-1]
dx = [0,0,-1,1,0,0]
for i in range(h):
    for j in range(n):
        arr[i][j]=list(map(int,input().split()))
def bfs(q):
    while q:
        z,y,x = q.popleft()
        for i in range(6):
            nh = z+dh[i]
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= nh < h and 0 <= ny < n and 0 <= nx < m:
                if arr[nh][ny][nx] == 0:
                    arr[nh][ny][nx] = arr[z][y][x]+1
                    q.append((nh,ny,nx))



q=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k]==1:
                q.append((i,j,k))
                bfs(q)
print(max(arr))