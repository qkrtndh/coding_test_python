
def check_2_friend():
    for i in range(n):
        crr=[0]*n
        for j in range(n):
            if arr[i][j]=='Y':
                crr[j]=1
                for k in range(n):    
                    if arr[j][k]=='Y':
                        crr[k]=1
        brr[i]=crr.count(1)
        if(crr[i]==1):
            brr[i]-=1

n=int(input())

arr=[]
brr=[0]*n

for i in range(n):
    arr.append(input())

check_2_friend()
print(max(brr))