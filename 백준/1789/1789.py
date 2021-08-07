s=int(input())
a=1
cnt=0
v=0
while 1:
    if s-v-a>a:
        v+=a
        a+=1
        cnt+=1
    elif s-v-a==a:
        cnt+=1
        break
    elif s-v-a<a:
        cnt+=1
        break
    
print(cnt)