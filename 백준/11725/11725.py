import sys
sys.setrecursionlimit(10**6)
def dfs(k):
    for i in arr[k]:
        if p[i]==0:
            p[i]=k
            dfs(i)

n = int(input())

arr=[[] for _ in range(n+1)]
p=[0 for _ in range(n+1)]
for i in range(n-1):
    s,o = map(int,sys.stdin.readline().split())
    arr[s].append(o)
    arr[o].append(s)

p[1]=-1
dfs(1)
for i in range(2,n+1):
    print(p[i])