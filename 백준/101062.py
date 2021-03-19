t = int(input())

A = 300
B = 60
C = 10

cnt = [0]*3
result=1
def divid(n,num):
    global t
    global cnt
    while t//num>0:
        cnt[n]+=t//num
        t%=num

while t>1:
    if t%C!=0:
        result = 0
        break
    if t//A>0:
        divid(0,A)
    if t//B>0:
        divid(1,B)
    if t//C>0:
        divid(2,C)
if result:
    print(cnt[0],cnt[1],cnt[2])
else:
    print(-1)