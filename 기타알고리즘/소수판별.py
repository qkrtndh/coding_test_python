#기본적인 알고리즘
def is_prime_number(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

#모든 수를 확인한다는 점에서 O(X)



"""
약수의 성질
모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이루는 것을 알 수 있다.
따라서 우리는 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 된다
"""
import math
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
#O(N^(1/2))


"""
다수의 소수 판별

에라토스테네스의 체 알고리즘

다수의 자연수에 대해 소수여부 판별에서 사용되는 대표적 알고리즘

N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다

1. 2부터 N까지의 모든 자연수를 나열한다
2. 남은 수 중에서 아직 처리하지 않은 가장 작은수 i를 찾는다
3. 남은 수 중에서 i를 제외한 i의 배수를 모두 제거한다
4. 더이상 반복할 수 없을 때 까지 2번과 3번의 과정을 반복한다

O(NloglogN)
각 자연수에 대한 소수여부를 저장해야 하므로 메모리가 많이 필요하다.

"""
import math

n = 1000

array = [True for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):
    if array[i]==True:
        j=2
        while i*j<=n:
            arr[i*j]=False
            j+=1
for i in range(2,n+1):
    if array[i]:
        print(i, end=' ')