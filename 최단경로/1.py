"""
N개의 도시가 있다.
각 도시는 보내고자 하는 메세지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 
해당 메세지를 전송할 수 있다.

하지만 x라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 
도시 x에서 y로 향하는 통로가 설치되어 있어야 한다

y에서 x로 향하는 통로는 있고
x에서 y로 향하는 통로가 없다면  x는 y로 보낼 수 없다

또한 통로를 거쳐 메세지를 보낼 때는 일정시간이 소요된다.

c도시에서 위급 상황이 발생하여 최대한 많은 도시로 메세지를 보내고자 한다
c에서 출발하여 각 도시 사이에 설치된 통로를 거쳐 최대한 많이 퍼져나갈 것이다

각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 
받게되는 도시의 개수는 총 몇개이며, 도시들이 메세지를 받는데 까지 걸리는 시간은 얼마인지
계산하는 프로그램을 작성하시오
"""

#입력
"""
첫째 줄에 도시의 개수 N, 통로의 개수 M 메시지를 보내고자 하는 도시C가 주어진다
1<=N<=30000   1<=m<=200,000, 1<=C<=N

둘째 줄 부터 M+1번째 줄에 걸쳐 통로에 대한 정보 X,Y,Z가 주어진다.
X에서 Y로 Z시간
1<=z<=1000
"""

#출력
"""
C에서 보낸 메시지를 받는 도시의 수와 총 걸리는 시간을 공백으로 구분하여 출력
"""

#아이디어
"""
한 도시에서 다른도시로의 최단거리, 또한 노드수가 많으므로 우선순위 큐를 사용한
다익스트라 알고리즘을 사용한다.
"""

import heapq

INF = int(1e9)

n,m,c = map(int,input().split())

graph = [[] for i in range(n+1)]

dist = [INF]*(n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        d, now = heapq.heappop(q)
        if d>dist[now]:
           continue
        for i in graph[now]:
            if d+i[1]<dist[i[0]]:
                dist[i[0]]=d+i[1]
                heapq.heappush(q,(dist[i[0]],i[0]))

dijstra(c)

cnt =0
maxi= 0
for i in dist:
    if i != INF and i!=0:
        cnt+=1
        maxi = max(maxi,i)
print(cnt, maxi)