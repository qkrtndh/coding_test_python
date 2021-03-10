"""
n*m크기의 미로에 갇혔다.
현재위치는 1,1이며, 출구는 n,m이다. 괴물의 위치는 0으로 없는 위치는 1로 표시된다.
탈출을 위해 움직여야 하는 최소 칸의 개수를 구하시오.
시작칸과 마지막칸을 포함해서 계산한다.
"""
#아이디어
"""
BFS로 갈 수 있는 곳을 미리 담고, 해당 위치의 값이 1이면 현재 크기를 더하고,
1이 아니라면 더한 값과 원래 값 중 더 작은 값을 유지시킨다.
그 후 변경한 위치에 대해서만 BFS를 다시 수행하고 결과적으로 nm에 도달했을 때의
값을 출력한다
"""

#아이디어 수정
"""
bfs로 갈수 있는 곳을 담으면서 뻗어 나가면 그것이 최단경로 이다.
즉 갈 수있는 곳의 숫자가 1이고, nm을 벗어나지 않는다면 현재 위치의 값과 계속
더해나가면 최단 거리를 구할 수 있다
bfs특성상 지나간 자리를 다시 지나갈때 값이 작아질 경우는 없다.
"""

#파이썬으로 bfs가 어색하여 거의 보면서 푼 것에 가까웠음
#해당 위치까지의 거리만 측정한 것이 아닌 모든 경로에 대한 측정이었음
#마지막에 해당위치의 거리만 따로 반환하였음.
from collections import deque

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if g[nx][ny]!=0 and g[nx][ny]==1:
                    q.append((nx,ny))
                    g[nx][ny]+=g[x][y]
    return g[n-1][m-1]
                    


n,m = map(int,input().split())
g=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    g.append(list(map(int,input())))

cnt = 1
print(bfs(0,0))