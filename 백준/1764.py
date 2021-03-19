n,m = map(int,input().split())
arr=set({})
brr=set({})
for i in range(n):
    arr.add(input())
for i in range(m):
    brr.add(input())
crr = list(arr & brr)
crr.sort()
print(len(crr))
for i in crr:
    print(i)