"""
정수 N이 입력되면 00시 00분 00초 부터 N시59분59초 까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라"""
n= int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            #if i//10==3 or i%10 ==3 or j//10==3 or j%10 ==3 or k//10==3 or k%10 ==3:
            if '3' in str(i) + str(j) + str(k):
                #시 분 초를 하나의 문자열로 한번에 만들어서 3이 포함되는지를 검사
                cnt+=1
print(cnt)