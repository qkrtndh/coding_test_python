"""
서로소 집합이란

공통원소가 없는  두 집합을 의미한다

서로소집합 자료구조
서로소 부분집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조

서로소 집합 자료구조는 두 종류의 연산을 지원한다

1. 합집합 : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산

2. 찾기 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

서로소 집합 자료구조는 합치기 찾기 자료구조로 불리기도 한다.

"""

"""
여러개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정은 다음과 같다

1. 합집합 연산을 확인하여 서로 연결된 두 노드 A,B를 확인한다
A, B 의 루트 노드 A' 와 B' 를 각각  찾는다
A'를 B'의 부모 노드로 설정한다

2. 모든 합집합 연산을 처리할 때 까지 1번의 과정을 반복한다.

작은 번호의 노드를 부모 노드로 설정하는 것이 관례처럼 사용됨
"""

"""
기본적인 형태의 서로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없다
루트노드 !=부모노드
루트노드를 찾기 위해 부모노드를 계속 거슬러 올라가야 한다.
"""

def find_parent(parent,x):
    if parent[x]==x:
        return x
    return find_parent(parent,parent[x])

def union_parent(parent,a ,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b
v, e = map(int,input().split())
parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b = map(int,input().split)
    union_parent(parent,a,b)

print("각 원소가 속한 집합")
for i in range(1,v+1):
    print(find_parent(parent,i))

print("부모테이블")
for i in range(1,v+1):
    print(parent[i])

"""
합집합 연산이 편향되게 이루어지는 경우 찾기 함수가 비효율적으로 동작한다
찾기함수를 최적화 하기 우해 경로압축을 사용할 수 있다
찾기 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 바로 갱신한다.
"""
def find_parent(parent,x):
    if parent[x]==x:
        return x
    return find_parent(parent,parent[x])

def find_parent(parent,x):
    if parent[x]==x:
        return x
    parent[x]=find_parent(parent,parent[x])
    return parent[x]

"""
서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다.
방향그래프 내에서의 사이클 여부는 DFS를 사용하면 된다

사이클 판별 알고리즘은 다음과 같다.

1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인한다
루트 노드가 서로 다르다면 두 노드에 대해 합집합 연산을 수행한다
루트 노드가 서로 같다면 사이클이 발생한 것이다

2. 그래프에 포함되어 있는 모든 간선에 대해 1번과정을 반복
"""


def find_parent(parent,x):
    if parent[x]==x:
        return x
    parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a ,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b
v, e = map(int,input().split())
parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i]=i

Cycle = False

for i in range(e):
    a,b = map(int,input().split)
    if find_parent(parent,a) == find_parent(parent,b):
        Cycle=True
        break
    union_parent(parent,a,b)


if Cycle:
    print("사이클 발생")
else:
    print("사이클 없음")

"""
신장 트리

그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다
모든노드가 포함되어 서로 연결되면서 사이크링 존재하지 않는다는 조건은 트리의 조건이기도 하다.


최소신장트리
최소한의 비용으로 구성되는 신장트리를 찾아야 할 때 사용
n개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 도시가 서로 연결될 수 있게
도로를 설치하는 경우

두 도시 A,B를 선택했을 때 A에서 B로가는 경로가 반드시 존재하도록 도로를 설치해야한다.

크루스칼 알고리즘
대표적인 최소신장트리 알고리즘

그리디알고리즘으로 분류된다.

1. 간선 데이터 비용에 따라 오름차순으로 정렬한다
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
 사이클이 발생하지 않는 경우 최소신장트리에 포함한다
 사이클이 발생하는 경우 최소 신장트리에 포함하지 않는다
3. 모든간선에 대해 2번을 반복한다


O(ElogE)
"""
def find_parent(parent,x):
    if parent[x]==x:
        return x
    parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a ,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b
v, e = map(int,input().split())
parent = [0]*(v+1)

edges=[]
result=0
for i in range(1,v+1):
    parent[i]=i


for i in range(e):
    a,b,cost = map(int,input().split())
    edges.append(cost,a,b)

edges.sort()

for edge in edges:
    cost, a,b = edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(result)
"""
위상정렬

사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열

진입차수 - 특정한 노드로 들어오는 간선의 개수

진출차수 - 특정한 노드에서 나가는 간선의 개수

위상정렬 알고리즘
일반적으로 DFS를 이용해 구현할 수 있다

큐를 이용하는 위상 정렬 알고리즘의 동작과정은 다음과 같다
1. 진입차수가 0인 모든 노드를 큐에 넣는다

2. 큐가 빌 때까지 다음의 과정을 반복한다
    큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다
    새롭게 진입차수가 0이된 노드를 큐에 넣는다

결과적으로 각 노드가 큐에 들어온 순서가 위성정렬을 수행한 결과와 동일하다.


위상정렬은 DAG(사이클이없는 방향그래프)에서만 수행가능

위상정렬에는 여러가지 답이 있을 수 있다

모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.

스택을 활용한 DFS를 이용해 위상정렬을 수행할 수 있다

O=(v+E)
"""

from collections import deque

v,e = map(int,input().split())

indegree=[0]*(v+1)

graph = [[]for i in range(v+1)]

for i in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now = q.popleft
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i,end=' ')
topology_sort()