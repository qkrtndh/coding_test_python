import sys
def find_parent(parent,x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_child(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
v,e = map(int,sys.stdin.readline().split())
parent = [0]*(v+1)
edges = []

for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
result = 0
edges.sort()
for edge in edges:
    cost, a,b = edge
    if find_parent(parent, a)!=find_parent(parent, b):
        union_child(parent,a,b)
        result +=cost
print(result)