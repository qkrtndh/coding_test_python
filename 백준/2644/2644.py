def dfs(s):
    cnt=0
    
    for i in range(1,n+1):
        if brr[i]==0 and arr[s][i]==1 and  i!=x and brr[y]==0:
            brr[i]=1
            cnt+=1
            if i==y:
                return cnt
            cnt+=dfs(i)
    if cnt == 0:
        return -1        
    return cnt;
    


n = int(input())
x,y=map(int,input().split())

arr =[[0 for _ in range(n+1)] for _ in range(n+1)]
brr =[0 for _ in range(n+1)]
m = int(input())

for _ in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1
print(dfs(x))