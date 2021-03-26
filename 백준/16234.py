from collections import deque
import sys
n,l,r=map(int,sys.stdin.readline().split())
q = deque()
arr=[]

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(i,j):
    q.append([i,j])
    brr=[]
    brr.append([i,j])
    while q:
        y,x = q.popleft();
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<n and visit[ny][nx]==0:
                if l <= abs(arr[ny][nx]-arr[y][x]) <= r:
                    q.append([ny,nx])
                    visit[ny][nx]=1
                    brr.append([ny,nx])
    return brr

cnt=-1
s=1
while s==1:
    cnt+=1
    visit = [[0] * n for _ in range(n)]
    s=0
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                visit[i][j]=1
                temp = bfs(i,j)
                if len(temp)>1:
                    s=1
                    k = sum([arr[a][b]for a, b in temp])//len(temp)
                    for a,b in temp:
                        arr[a][b]=k
    if s==0:
        break
                
print(cnt)