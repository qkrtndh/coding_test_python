"""
리스트에 순차적으로 접근해야 할 때 두개의 점의 위치를 기록하면서 처리하는 알고리즘

리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 시작점과 끝점 2개의 점으로
접근할 데이터의 범위를 표현할 수 있다.
"""

"""
N개의 자연수로 구성된 수열이 있습니다
합이M인 부분 연속 수열의 개수를 구해보세요
수행 시간 제한은 O(N)입니다.
"""

"""
1. 시작점과 끝점을 0을 가리키도록한다
2. 현재 부분 합이 M과 같다면 카운트한다
3. 현재 부분합이 M보다 작다면 end를 1증가시킨다
4. 현재 부분 합이 M보다 크거나 같다면 start를 1증가시킨다
5. 모든 경우를 확인할 때 까지 2번부터 4번까지의 과정을 반복한다
"""
n = 5
m = 5
data = [1,2,3,2,5]
count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end <n:
        interval_sum+=data[end]
        end+=1
    if interval_sum==m:
        count +=1
    interval_sum -= data[start]
print(count)