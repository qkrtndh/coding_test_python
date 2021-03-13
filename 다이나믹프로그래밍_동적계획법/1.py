"""
개미가 메뚜기의 식량창고를 턴다.
메뚜기의 식량창고는 여러개로 일직선으로 이어져있다.

각 식량창고에는 정해진  수의 식량을 저장하고 있으며 개미는 식량창고를 선택적으로
약탈하여 식량을 턴다.

메뚜기정찰병은 일직선상에 존재하는 식량창고 중 서로인접한 식량창고가 공격받으면
알 수 있다.

개미는 정찰병에게 걸리지 않고 약탈하기 위해선 최소 한칸 이상 떨어진 창고를
털어야 한다.

창고 n개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하라
"""

#입력
"""
첫째 줄에 창고의 수 n이 주어진다
3<=n<=100
둘째줄에 공백을 기준으로 각 창고에 저장된 식량의 수 K가 주어진다.
0<=k<=1000
"""

#출력
"""
털 수 있는 식량의 최댓값
"""

#아이디어
"""
문제를 상향식으로 접근한다.
1번창고부터 n번창고까지 하나씩 반복하면서 n번째 창고에서의 최대값을 저장해 나간다.
n번째와 n-2의 합과n-1의 합을 비교하여 높은쪽을 선택한다.
"""

#나의 풀이
"""
n = int(input())
wh = list(map(int,input().split()))
check = [0]*100
check[0]=wh[0]
check[1]=wh[1]
for i in range(2,n):
    if wh[i]+check[i-2]<check[i-1]:
        check[i]=check[i-1]
    else:
        check[i]=wh[i]+check[i-2]
print(check[n-1])
"""

#모범 답안
n = int(input())
wh = list(map(int,input().split()))
check = [0]*100
check[0]=wh[0]
check[1]=max(wh[0],wh[1])
for i in range(2,n):
    check[i] = max(wh[i]+check[i-2],check[i-1])
print(check[n-1])