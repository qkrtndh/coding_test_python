import sys
input = sys.stdin.readline#빠른 입력을 위해

minval=10000000000 #최소값을 가장 큰 값으로 설정
maxval=-1000000000 #최대값을 가장 작은 값으로 설정

n=int(input()) #수의 개수
numbers=list(map(int,input().split())) #숫자들
arr=list(map(int,input().split())) #+,-,*,/ 갯수

def calc(num,calced,a,b,c,d): #n번째 숫자 num, 이전 호출에서 계산된 값, abcd=사칙연산 갯수
    global minval,maxval #최대,최소값의 전역벽수화
    if num==n-1: #마지막 값인 경우(calc에 num+1과의 계산 값이 있으므로 n-1과 비교) 최대최소 입력
        maxval=max(maxval,calced)
        minval=min(minval,calced)

    #이하 식들을 else를 사용하지 않음으로서 모든 계산의 경우에 대해 진행

    if a!=0: #+연산이 남은경우
        calc(num+1,calced+numbers[num+1],a-1,b,c,d)

    if b!=0: #-연산이 남은경우
        calc(num+1,calced-numbers[num+1],a,b-1,c,d)

    if c!=0: #*연산이 남은경우
        calc(num+1,calced*numbers[num+1],a,b,c-1,d)

    if d!=0: #/연산이 남은경우
        if calced<0: #만약 음수를 나누는 경우
            temp = (-1)*calced//numbers[num+1] #양수화
            temp = (-1)*temp #결과 음수화

        else: 
            temp = calced//numbers[num+1] #양수인경우 바로 연산

        calc(num+1,temp,a,b,c,d-1) #연산값 대입 후 진행

    
#초기 index 0,  처음숫자  ,+,-,*,/ 개수
calc(0,numbers[0],arr[0],arr[1],arr[2],arr[3])
print(maxval)
print(minval)



