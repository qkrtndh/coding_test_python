"""
어떤수 x가 주어질 때 할 수 있는 연산은 다음과 같다
1. 5로 나누어 떨어지면 5로 나눈다
2. 3으로 나누어 떨어지면 3으로 나눈다
3. 2로 나누어 떨어지면 2로 나눈다.
4. 1을 뺀다

x가 주어질때 4가지 연산을 사용하여 1로 만드는 최소 연산횟수를 구하라.
"""

#입력
"""
첫째줄에 정수 x가 주어진다
1<=x<=30000
"""

#출력
"""
최소 연산 횟수를 출력한다.
"""

#아이디어
"""
x를 나누어 떨어지는 수들의 모음으로 생각하면 작은문제들의 집합으로 볼 수 있다
따라서 1부터 x까지의 수들의 최소 연산수를 비교하면 구할 수 있다.
"""
#d는 해당 index 숫자의 최소 연산 횟수
#d[2]는 1 2를 1로 나누거나 1로 빼면 1번의 연산으로 1이 되므로 1이다.
d=[0]*30001
x = int(input())
for i in range(2,x+1):
    d[i]=d[i-1]+1#d[i]는 d[i-1]즉 예를들어 3인경우는 1을 빼는 연산(+1)과 2의 연산수의 합
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)#각 나누기 는 나눈 수의 최소연산수 +1나누기연산
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)    
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[x])

#추후 복습 필요. 보고푼것에 가까움