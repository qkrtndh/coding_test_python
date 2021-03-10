#어떤 수 N이 1이 될때 까지 1을 빼거나 K로 나눈다. 나누기는 나누어 떨어질때만 가능하다.

#내가 쓴 코드
"""
n,k=map(int,input().split())

cnt = 0
while(n!=1):
  if n%k==0:
    n//=k
  else:
    n-=1
  cnt+=1
print(cnt)
"""
#모범?답안
n,k = map(int,input().split())
result = 0
while True:
    #target은 n에서 가장 가까운 k와 나누어 떨어지는 수 이다.
    target = (n//k)*k
    #n에서 target차이 만큼 1을 빼므로 그 차를 횟수에 더하면 반복문을 덜 돌면서 1을빼는
    #연산 횟수를 구할 수 있다.
    result += (n-target)
    #1을 뺀 후 나누기가 가능해진 상태가 된다.
    n=target
    #만일 k보다 작아지면 나눌 수 없이 빼기만 가능하므로 탈출한다
    if n<k:
        break
    #나누기가 가능한 경우 횟수를 올리고 값을 바꾼다.
    result +=1
    n//=k
#1보다 크고 나누기가 불가능 한 경우 1과의 차이만큼 1을 빼는 연산이 진행된다.
result+=(n-1)
print(result)