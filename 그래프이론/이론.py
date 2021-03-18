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