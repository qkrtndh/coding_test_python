"""
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
이 수열에서 X가 등장하는 횟수를 계산하라.
O(logN)으로 알고리즘을 설계하지 않으면 시간초과 판정을 받는다.
"""

#입력
"""
첫째 줄에 정수의 수 n과 찾는 수 x가 입력된다.
둘째 줄에 공백으로 구분되어 n개의 정수가 입력된다.
"""
#출력
"""
원소x의 개수를 출력한다.
단 없다면 -1을 출력한다
"""

#아이디어
"""
bisect를 사용하면 간단하게 해결할 수 있다.
"""
"""
from bisect import bisect_left,bisect_right

n,x = map(int,input().split())
arr = list(map(int,input().split()))
r=bisect_right(arr,x)-bisect_left(arr,x)
if  r== 0:
    print(-1)
else:
    print(r)

"""
#이진탐색으로 풀어보기
n,x = map(int,input().split())
arr = list(map(int,input().split()))

def left_search(arr,s,e,t):
    mid = (s+e)//2
    if(s>e):
        return None
    if t == arr[s]:
        return s
    elif arr[mid]>=t:
        return left_search(arr,s+1,mid,t)
    else:
        return left_search(arr,mid+1,e,t)

def right_search(arr,s,e,t):
    mid = (s+e)//2
    if(s>e):
        return None
    if t == arr[e]:
        return e
    elif arr[mid]>t:
        return right_search(arr,s,mid-1,t)
    else:
        return right_search(arr,mid,e-1,t)
        
r1 = left_search(arr,0,len(arr)-1,x)
r2 = right_search(arr,0,len(arr)-1,x)

if r2==None or r1==None:
    print(-1)
else:
    print(r2-r1+1)
    