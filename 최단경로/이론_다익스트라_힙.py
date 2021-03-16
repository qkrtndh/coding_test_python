"""
가장 짧은 경로를 찾는 알고리즘

한 지점에서 다른 한 지점까지 최단경로
한 지점에서 다른 모든 지점까지의 최단 경로
모든 지점에서 다른 모든 지점까지의 최단 경로

각 지점은 그래프에서 노드로 표현
지점간 연결된 도로는 그래프에서 간선으로 표현

다익스트라 알고리즘
특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
음의 간선이 없을 때 정상적으로 동작한다.
그리디 알고리즘으로 분류된다.
= 매 상황에서 가장 비용이 적게 드는 노드를 선택해 임의 과정을 반복한다.

알고리즘 동작 과정
1. 출발 노드를 설정한다
2. 최단 거리 테이블을 초기화한다
 - 모든 노드까지의 거리는 무한으로, 자신으로는 0으로 설정
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐서 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 3,4를 반복한다

전체 시간 복잡도는 O(v^2)
전체 노드가 5000개 이하라면 이 방법으로 해결할 수 있다.
"""
"""
import sys
input = sys.stdin.readline

INF = int(1e9)#10억 무한으로 상정함

#노드수, 간선 수 입력
n,m = map(int,input().split())

#시작노드
start = int(input())

#0번노드 안쓰고 n개의 리스트를 같는 그래프
#각 리스트는 목적지와 간선의 길이
graph = [[]for i in range(n+1)]

#방문정보 리스트
visited = [False]*(n+1)

#거리정보 리스트 처음엔 무한으로
distance = [INF]*(n+1)


#
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1,n+1):
        if distance[i]<min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]]=i[1]
    for i in range(n-1):
        index = get_smallest_node()
        visited[index] = True
        for j in graph[index]:
            if (distance[index]+j[1]) < distance[j[0]]:
                distance[j[0]] = distance[index]+j[1]
dijkstra(start)

for i in range(1,n+1):
    if distance[i]!=INF:
        print(str(i)+': ',end='')
        print(distance[i])
"""


"""
노드가 5000초과일 경우

우선순위 큐
우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
표준 라이브러리 형태로 지원한다.

힙
우선순위 큐를 구현하기 위해 사용되는 자료구조 중 하나이다.
최소 힙과 최대 힙이 있다.
다익스트라 최단 경로 알고리즘을 포함하여 다양한 알고리즘에서 사용된다

우선순위 큐 구현 방식       삽입 시간       삭제시간

리스트                        O(1)         O(N)

힙                           O(loN)       O(loN)

"""

#힙 정렬

#최소힙
#기본적으로 내림차순, 우선순위가 낮은 것 부터 되어있으므로 오름차순으로 만든다
#단순히 넣을때 내림차순인므로 그대로 꺼내면 오름차순이 된다.
"""
import heapq

def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#최대힙
#달리 최대힙을 지원하지 않음으로 넣을때 와 꺼낼때 부호를 바꾸는 것으로 구현 가능하다
#내림차순 정렬
import heapq

def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
"""

"""
개선된 다익스트라 알고리즘

단계마다 방문하지 않은 노드 중에서 최단 거리가
가장 짧은 노드를 선택하기 위해 힙 자료구조를 사용한다.

기본 원리는 동일하다.
가장 가까운 노드를 저장하기 위해 힙 자료구조를 사용하는 부분이 다르다.
현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용한다
"""


import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)#10억 무한으로 상정함

#노드수, 간선 수 입력
n,m = map(int,input().split())

#시작노드
start = int(input())

#0번노드 안쓰고 n개의 리스트를 같는 그래프
#각 리스트는 목적지와 간선의 길이
graph = [[]for i in range(n+1)]


#거리정보 리스트 처음엔 무한으로
distance = [INF]*(n+1)


#
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    #시작노드에서 시작노드로 가는 최단 경로는 0
    heapq.heappush(q,(0,start))
    distance[start] = 0
    #큐가 있는 동안
    while q:
        #가장 거리가 짧은 노드 정보 출력 (거리, 목적지)
        dist, now = heapq.heappop(q)

        #방문한 적 있으면 무시
        if distance[now]<dist:
            continue
        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))


dijkstra(start)

for i in range(1,n+1):
    if distance[i]!=INF:
        print(str(i)+': ',end='')
        print(distance[i])