"""
미래 도시에는 1부터 N번까지의 회사가 있다.
특정 회사끼리는 서로 도로를 통해 연결되어있다

방문판매원 A는 현재 1번 회사에 위치해 있으며 x번 회사에 방문해 물건을 판매하고자 한다

특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는
방법이 유일하다.

또한 연결된 2개의 회사는 양방향으로 이동할 수 있다.
특정 회사와 다른 회사가 연결되어 있는 경우 1만큼의 시간에 이동할 수 있다

A는 소개팅에도 참석하려고 한다 소개팅상대는 K번째 회사에 존재한다.
방문판매원 A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의 회사에
찾아가서 함께 커피를 마시려고 한다

따라서 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표다.

이 때 방문 판매원 A는 가능한 한 빠르게 이동하고자 한다.

방문판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오

"""

#입력
"""
첫째 줄에 전체 회사의 개수 N과 경로의 수 M이 공백으로 구분되어 주어진다
둘째 줄 부터 연결된 두 회사의 번호가 공백으로 구분되어 주어진다
마지막 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다
1<=N,M,K<=100
"""

#출력
"""
A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다
만약 도달할 수 없다면 -1을 출력한다
"""

#아이디어
"""
플로이드 워셜 알고리즘을 사용한다.
"""
INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1)for i in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
x,k = map(int,input().split())
for f in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][f]+graph[f][j])

if graph[x][k]!=INF:
    print(graph[1][k]+graph[k][x])
else:
    print(-1)