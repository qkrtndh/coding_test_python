from bisect import bisect_left,bisect_right
import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))

m = int(input())
brr = list(map(int,sys.stdin.readline().split()))

arr.sort()
for i in range(m):
    c= bisect_right(arr,brr[i])-bisect_left(arr,brr[i])
    print(c,end=' ')