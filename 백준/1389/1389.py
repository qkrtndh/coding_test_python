def BFS(num):
    q=[]
    brr =[0 for _ in range(n+1)]
    brr[num]=0
    q.append(num)
    while q:
        x=q.pop(0);
        for i in range(1,n+1):
            if arr[x][i]==1 and brr[i]==0 and num!=i:
    
                brr[i]+=brr[x]+1
                q.append(i)
    return sum(brr)




n,m = map(int,input().split())
arr =[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1
value = 1000000
k=101
for i in range(1,n+1):
    cnt = BFS(i)
    if cnt<value:
        value=cnt
        k=i
print(k)