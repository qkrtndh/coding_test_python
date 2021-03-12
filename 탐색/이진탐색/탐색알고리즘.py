#이진탐색 O(log N)
def binary_search(arr,target,s,e):
    mid = (s+e)//2
    if s>e:
        return "없습니다"
    if target<arr[mid]:
        return binary_search(arr,target,s,mid-1)
    elif target>arr[mid]:
        return binary_search(arr,target,mid+1,e)
    elif target == arr[mid]:
        return mid+1 
    

#n ,target = map(int,input().split())
#arr = list(map(int,input().split()))
#print(binary_search(arr,target,0,len(arr)))

#bisect
from bisect import bisect_left,bisect_right
def count_by_range(a,l,r):
    lv=bisect_left(a,l)
    rv=bisect_right(a,r)
    return rv-lv
a=[1,2,3,3,3,3,4,4,8,9]
#4의 개수
print(count_by_range(a,4,4))

#-1~3의 개수
print(count_by_range(a,-1,3))

#파라메트릭 서치(parametric search)
"""
최적화 문제를 결정문제(예,아니오)로 바꾸어 해결하는 기법이다.
최적화 문제 :특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 문제
여러번의 결정문제로 나누어 빠르게 찾는다

이진탐색으로 해결할 수 있다.
"""