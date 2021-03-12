"""
두개의 배열 A,B N개의 원소로 구성되어 있으며 모두 자연수 있다.

K개의 바꿔치기 연산을 수행할 수 있다
바꿔치기 연산은 배열 A에 있는 원소 하나와 B에있는 원소 하나를 골라 서로 교환하는 것이다.

배열 A의 모든 원소의 합이 최대가 되도록 한다.

N,K, A,B의 정보가 주어질 때 최대 K번의 바꿔치기 연산을 수행하여
만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오
"""

#나의 풀이
"""
n,k = map(int,input().split())
arr=list(map(int,input()))
brr=list(map(int,input()))
arr.sort()
brr.sort(reverse=True)

i=0
j=0
while(k>0 and i<len(arr) and j < len(brr)):
    if arr[i]<brr[j]:
        k-=1
        arr[i],brr[j]=brr[j],arr[i]
    i+=1
    j+=1

print(sum(arr))
"""
#모범?
n,k = map(int,input().split())
arr=list(map(int,input()))
brr=list(map(int,input()))
arr.sort()
brr.sort(reverse=True)

for i in range(k):
    if arr[i]<brr[i]:
        arr[i],brr[i]=brr[i],arr[i]
    else:
        break

print(sum(arr))