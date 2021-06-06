import sys
n = int(input())
arr=[[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int,sys.stdin.readline().split()))
arr.sort()
temp=0
cnt=1
for i in range(1,n):
    if arr[temp][1]<=arr[i][0]:
        temp=i
        cnt+=1
    elif arr[temp][0]<=arr[i][0] and arr[temp][1]>=arr[i][1]:
        temp=i
print(cnt)