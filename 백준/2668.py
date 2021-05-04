n=int(input())

arr=[] 
brr=[]
crr=[]
arr.append(100)
brr.append(100)
for i in range(1,n+1):
    arr.append(int(input()))
    brr.append(0)

maxval = 1
for i in range(1,n+1):
    brr[i]=1
    crr.append(i)
    if brr[arr[i]]==0:
        
        maxval+=1
        i=arr[i]
        
print(maxval)
print(crr)