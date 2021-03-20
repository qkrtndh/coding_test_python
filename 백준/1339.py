n = int(input())

arr=[]
num=[]
dic = {}
for i in range(n):
    arr.append(input())
    l = len(arr[i])-1
    for j in arr[i]:
        if j in dic:
            dic[j]+=pow(10,l)
        else:
            dic[j]=pow(10,l)
        l-=1

for i in dic.values():
    num.append(i)
num.sort(reverse=True)

k=9
for i in range(len(num)):
    num[i]*=k
    k-=1
print(sum(num))