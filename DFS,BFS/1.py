"""
N*M의 얼음틀이 있다.
구멍이 뚫린부분은 0 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫린 부분 끼리는 상하좌우로 붙어있는 경우 서로 연결된 것으로 간주한다.
이때 얼음 틀의 모양이 주어질 때 생성되는 총 아이스크림의 수는?"""
#첫줄에 n과 m이, 둘쨋줄부터 얼음틀의 모양이 주어진다.

#아이디어
"""
틀 전체를 훑어서 0인 부분을 기준으로 dfs를 하여 dfs를 한 횟수를 출력한다
"""
"""
def dfs(i,j):
    g[i][j]=1
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if g[nx][ny]==0:
                dfs(nx,ny)


n,m=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
g=[]
cnt = 0
for i in range(n):
    g.append(list(map(int,input())))
for i in range(n):
    for j in range(m):
       if g[i][j]==0:
           cnt+=1
           dfs(i,j)
print(cnt)
"""

#답안 코드
def dfs(i,j):
    if i<=-1 or i>=n or j>=m or j<=-1:
        return False
    if g[i][j]==0:
        g[i][j]=1
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)
        return True
    return False

n,m=map(int,input().split())
g=[]
cnt = 0
for i in range(n):
    g.append(list(map(int,input())))
for i in range(n):
    for j in range(m):
       if dfs(i,j) == True:
           cnt+=1
print(cnt)