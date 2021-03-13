"""
n*m크기의 금광이 있다 각 금광은 1*1크기로 나누어져 있으며 각 칸은
특정한 크기의 금이 들어있다.

채굴자는 첫번째 열에서 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 열의
어느행에서든 출발할 수 있다.

이후에 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽 , 오른쪽 아래 
3가지 중 한 방향으로 이동해야 한다.

결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라
"""

#입력
"""
첫째 줄에 테스트 케이스 T가 주어진다
매 테스트 케이스 첫줄에 n,m이 공백으로 구분되어 입력된다
1<=n,M<=20

테스트 케이스 둘째줄에 n*m개의 금의 개수가 공백으로 구분되어 입력된다
1<=  <= 100
"""

#출력
"""
테스트 케이스마다 얻을 수 있는 금의 최대 크기를 출력한다.
각 테스트 케이스의 결과는 줄바꿈으로 구분한다
"""

#아이디어
"""
dx,dy를 사용하여 d의 현재값과 이전값과 원래값의 합중 큰것을 골라 갱신한다.
가장 마지막에 d에서 가장 큰 값을 찾는다.
"""

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    d=[]
    index = 0
    for j in range(n):
        d.append(arr[index:index+m])
        index+=m
    for j in range(1,m):
        for k in range(n):
            if k==0:
                lt=0
            else:
                lt = d[k-1][j-1]
            if k==n-1:
                lb = 0
            else:
                lb = d[k+1][j-1]
            l=d[k][j-1]
            d[k][j]=d[k][j]+max(lt,lb,l)
    maximum=0
    for j in range(n):
        maximum = max(maximum,d[j][m-1])
    print(maximum)
