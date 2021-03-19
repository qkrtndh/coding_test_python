"""
구간합 문제
연속적으로 나열된 N개의 수가 있을 때
특정 구간의 모든 수를 합한 값을 계산하는 문제

N개의 정수로 구성된 수열이 있다
M개의 각 쿼리 정보가 주어진다
각 쿼리는 left정보와 right 정보로 구성된다
각 쿼리에 대해 [left,right]구간에 포함된 데이터들의 합을 출력해야 한다

수행시간 제한은 O(m+n)
"""
"""
접두사 합을 사용한다.
접두사합은 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해놓은 것이다.

접두사 합을 활용한 알고리즘은 다음과 같다
N개의 수 위치 각각에 대하여 접두사 합을 계산하여 P에 저장한다.
매 M개의 쿼리 정보를 확인할 때 구간합은 p[right]-P[left-1]이다.
"""

n=5
data = [10,20,30,40,50]

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append[sum_value]

left = 3
right = 4
print(prefix_sum[right]-prefix_sum[left-1])