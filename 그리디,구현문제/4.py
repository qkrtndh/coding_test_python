"""
여행가 A는 NxN 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1x1크기의
정사각형으로 나누어져 있습니다. 가장 왼쪽 위 좌표는 1,1 이며 가장 오른쪽 아래는 N,N에 해당합니다.
여행가는 상하좌우로 이동할 수 있으며 시작 좌표는 항상 1,1입니다.

계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 반복적으로 적혀 있습니다.
각 문자의 의미는 좌,우,상,하 이동입니다
이때 NxN을 벗어나는 움직임은 무시됩니다.

여행자의 계획서대로 움직일 때 최종위치를 출력하라."""

"""
dx = [-1,1,0,0]
dy = [0,0,-1,1]

nx = 1
ny = 1
k=0
n=int(input())
X = list(map(str,input().split()))
for i in X:
    if i == 'L':
        k=2
    elif i =='R':
        k=3
    elif i =='U':
        k=0
    elif i =='D':
        k=1
    if(1<=(nx+dx[k])<=n and 1<=(ny+dy[k])<= n):
        nx=nx+dx[k]
        ny=ny+dy[k]
print(nx,ny)"""

dx = [-1,1,0,0]
dy = [0,0,-1,1]
#dx,dy 와 LRUD의 순서를 같게 한다.
move = ['U','D','L','R']
x = 1
y = 1
n=int(input())
X = list(map(str,input().split()))
for i in X:
    # 위의 if문 4개와 완전히 같은 역할을 한다.
    for j in range(len(move)):
        if move[j]==i:
            nx = x+dx[j]
            ny = y+dy[j]
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    x,y = nx,ny
print(nx,ny)