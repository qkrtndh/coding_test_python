"""
한 마을에 모험가 N명이 있다.
모험가 길드에서는 N명의 모험가를 대상으로 공포도를 측정했는데,
공포도가 높은 모험가는 쉽게 공포를 느껴 위험상황에서 제대로 대처할 능력이 떨어진다.

공포도가 X인 모험가는 반드시 X명 이상으로 구성된 그룹에 참여해야 한다.

N명의 모험가에 대한 정보가 주어질 때 여행을 떠날 수 있는 그룹의 수의
최댓값을 구하는 프로그램을 작성하라"""


"""
n= int(input())
X = list(map(int,input().split()))

max = int(X[0])
cnt = 1
sum = 0
for i in range(1,len(X)):
    num = int(X[i])
    if(cnt==max):
        cnt=1
        sum +=1
        max=num
    if num>max:
        max = num
    cnt+=1
print(sum)
"""
n= int(input())
X = list(map(int,input().split()))
#오름차순 정렬
X.sort()

cnt = 0#모험가 수
sum = 0#그룹 수
for i in X:
    cnt+=1#현재 그룹의 모험가 수 증가
    if cnt>=i:#어차피 오름차순 이기 때문에 같거나 큰 수만 들어옴, 수와 공포도가 같다면 그룹 생성
        sum+=1#그룹생성, 그룹에 추가되더라도 결성조건이 만족 되어야 추가됨
        cnt=0#인원수 초기화
    
print(sum)