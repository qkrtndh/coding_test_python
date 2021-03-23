n,m = map(int,input().split())
arr = list(map(int,input().split()))
plus,minus = [], []
for i in range(n):
    if arr[i]<0:
        minus.append(arr[i])
    else:
        plus.append(arr[i])
minus.sort()
plus.sort()
switch = 0
if max(plus)<min(minus)*(-1):
    if len(plus)%m!=0: