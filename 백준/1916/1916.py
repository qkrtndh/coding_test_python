import heapq
import sys
input = sys.stdin.readline

def dijstra(start):
    h=[]
    heapq.heappush(h,(0,start))
    dist[start]=0
    while(h):
        weight,node = heapq.heappop(h)
        if(dist[node]<weight):
            continue
        for i in g[node]:
            if i[1]+weight<dist[i[0]]:
               dist[i[0]] = i[1]+weight
               heapq.heappush(h,(dist[i[0]],i[0]))

INF = int(1e9)

n=int(input())
m=int(input())


g=[[] for i in range(n+1)]
dist=[INF]*(n+1)

for _ in range(m):
    x, y, z = map(int,input().split())
    g[x].append((y,z))

start, end = map(int,input().split())

dijstra(start)
print(dist[end])