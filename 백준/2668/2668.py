def brr_reset():
    for i in range(1,n+1):
        brr[i]=0

n=int(input())

arr=[] 
brr=[]
crr=[]
arr.append(101)
brr.append(101)
for i in range(1,n+1):
    arr.append(int(input()))
    brr.append(0)

for i in range(1,n+1):
    j=i
    brr_reset()
    brr[i]=0
    while(1):
        if brr[arr[j]]==0:
            brr[arr[j]]=1
            j=arr[j]
        else:
            if j==i:
                crr.append(i)
            break
print(len(crr))
for i in crr:
    print(i)
