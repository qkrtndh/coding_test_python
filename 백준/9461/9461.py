T=int(input())
number=[1,1,1]
arr=[]
for i in range(T):
    arr.append(int(input()))
for i in range(100):
    number.append(number[i]+number[i+1])
for i in range(T):
    print(number[arr[i]-1])