"""
모든 노드에서 다른 모든 노드 까지의 최단경로를 모두 계산
다익스트라 알고리즘과 마찬가지로 단계별로 거쳐가는 노드를 기준으로 알고리즘 수행

매 단계마다 방문하지 않은 노드 중 최단거리를 갖는 노드를 찾을 필요 없음

2차원 테이블에 최단 거리 정보를 저장한다
다이나믹 프로그래밍 유형에 속한다.

O(n^3)이며, 점화식은
D_ab  = min(D_an,D_ak+D_kb)
a에서 b로가는 최단 거리보다 a에서 k를 거쳐 b로가는 거리가 더 짧은지 검사한다.
"""

INF = int(1e9)

#노드수와 간선 수 
n=int(input())
m = int(input())

#2차원 리스트(그래프표현)를 만들고 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신은 0으로
for a in range (1, n+1):
    graph[a][a]=0

for _ in range(m):
    #a에서 b로 가는 비용 c
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print ("INF",end=" ")
        else:
            print(graph[i][j],end=" ")
    print()