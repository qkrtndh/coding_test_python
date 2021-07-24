n,m = map(int,input().split())
dy=[0,-1,0,1]
dx=[-1,0,1,0]

def bfs():
    visit=[[0 for _ in range(m)]for _ in range(n)]
    array = []
    array.append((0,0))
    visit[0][0]=1
    while array:
        x=array.pop(0)
        for i in range(4):
            cy=x[0]+dy[i]
            cx=x[1]+dx[i]
            if 0<=cy<n and 0<=cx<m:
                if arr[cy][cx]!=0:
                    arr[cy][cx]+=1
                elif arr[cy][cx]==0 and visit[cy][cx]==0:
                    visit[cy][cx]=1
                    array.append((cy,cx))

arr=[]
cnt=0
for i in range(n):
    brr=list(map(int,input().split()))
    arr.append(brr)

while 1 in sum(arr,[]):
    
    bfs()
    for i in range(n):
        for j in range(m):
            if arr[i][j]>2:
                arr[i][j]=0
            elif arr[i][j]==2:
                arr[i][j]=1
    cnt+=1
print(cnt)