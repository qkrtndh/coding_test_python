#선택정렬O(N^2)
arr = [3,4,1,7,8,5,6,9,2,0]
for i in range(10):
    index=i
    for j in range(i+1,10):
        if arr[j]<arr[index]:
            index=j
    arr[i],arr[index] = arr[index],arr[i]
#print(arr)

#삽입정렬 O(N^2  ~  N)
arr = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
#print(arr)

#퀵정렬 O(nlogn) ~ O(n^2)
arr = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(start,end,arr):
    if start>=end:
        return
    pivot = start
    l=start + 1
    r = end
    while l<=r:
        while l<=end and arr[l]<=arr[pivot]:
            l+=1
        while r>start and arr[r]>=arr[pivot]:
            r-=1
        if l<=r:
            arr[l],arr[r]=arr[r],arr[l]
        else:
            arr[r],arr[pivot]=arr[pivot],arr[r]
    quick_sort(start,r-1,arr)
    quick_sort(r+1,end,arr)

quick_sort(0,len(arr)-1,arr)
#print(arr)

#퀵정렬 파이썬 버전
arr2 = [5,7,9,0,3,1,6,2,4,8]
def quick_sort2(arr2):
    if len(arr2)<2:
        return arr2
    pivot = arr2[0]
    tail = arr2[1:]
    left_list = [x for x in tail if x<=pivot]
    right_list = [x for x in tail if x>pivot]
    return quick_sort2(left_list)+[pivot]+quick_sort2(right_list)
print(quick_sort2(arr2))

#계수정렬 O(N+K)
#데이터 크기 범위가 제한되어 정수형태로 표현 가능할 때 사용
#데이터 개수 N 최댓값이 K

arr= [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]*(max(arr)+1)
for i in arr:
    count[i]+=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')