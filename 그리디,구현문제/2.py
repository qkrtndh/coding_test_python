"""각 자리가 숫자 0~9로만 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 하나 씩 모든 숫자를 확인하며 숫자 사이에 X 혹은 + 연산자를 넣어
결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하라
단 +보다 X를 먼저 계산하지 않고 왼쪽부터 순서대로 이루어진다."""


#나의 답
"""
n=input()
result = 0
for i in n:
    if i=='0' or result == 0 or i=='1' or result == 1:
        result+=int(i)
    else:
        result*=int(i)
print(result)
"""
n=input()
result = int(n[0])
for i in range(1,len(n)):
    num = int(n[i])
    if result<=1 or num<=1:
        result+=num
    else:
        result*=num
print(result)