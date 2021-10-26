import sys
input = sys.stdin.readline
def checktree(i):
    if visit[i] == 0:
        visit[i]=1
        node=[i]
        while node:
            now=node.pop(0)
            for j in range(1,n+1):
               if route[now][j]==1:
                    if visit[j] == 0:
                        visit[j]=1
                        route[now][j]=0
                        route[j][now]=0
                        node.append(j)
                    else:
                        return -1
        return 1
    return 0            
case=0
while 1:
    case+=1
    n,m=map(int,input().split())
    if(n==0 and m==0): break
    result=0
    visit=[0]*(n+1)
    route=[[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        route[a][b]=1
        route[b][a]=1
    for i in range(1,n+1):
        result+=checktree(i)
    print("Case %d:"%(case),end='')
    if(result <= 0):
        print("No trees.")
    elif(result == 1):
        print("There is one tree.")
    else:
        print("A forest of %d trees."%(result))