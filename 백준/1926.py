import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    arr[y][x] = 0
    size = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx <m and 0<= ny <n:
            if arr[ny][nx]==1:
                size +=dfs(nx,ny)
    return size
n,m = map(int,input().split())
arr = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in range(n):
    arr.append(list(map(int,input().split())))

max_size = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            cnt+=1
            max_size = max(max_size,dfs(j,i))
print(cnt)
print(max_size)