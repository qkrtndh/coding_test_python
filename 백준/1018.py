def check(i,j):
    w=0
    b=0
    for k in range(i,i+8):
        for l in range(j,j+8):
            if (k+l)%2 == 0:
                #W로 시작한 경우
                if arr[k][l]!='W':
                    w+=1
                #B로 시작한 경우
                else:
                    b+=1
            else:
                #W로 시작한 경우
                if arr[k][l]!='B':
                    w+=1
                #B로 시작한 경우
                else:
                    b+=1

    brr.append(w)
    brr.append(b)
n,m = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(input())
brr=[]
right = m-8
bottom = n-8
for i in range (bottom+1):
    for j in range(right+1):
        check(i,j)
print(min(brr))
