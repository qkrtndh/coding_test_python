<H1>1058</H1>

![image](https://user-images.githubusercontent.com/65153512/120090568-9fea5600-c13e-11eb-9392-656631d33914.png)

친구 관계가 배열로 입력되며
2단계에 걸쳐 친구관계를 확인하여 친구수를 별도의 배열에 저장한 후 가장 큰 값을 출력한다.

i 번째 반복문으로 1차 친구들을 검사한다. 
친구인경우 i번째 사람의 친구관계 배열 crr에 j번째 친구를 1로 카운트한다.
그 후 2차친구 검사를 진행한다.
j번째 친구의 친구 k들을 마찬가지로 crr에 1로 변경한다.

i번째 사람의 처리가 끝나면 crr의 1들을 센 뒤 자기 자신이 카운트된 경우를 제외하여
brr에 그 값을 저장한다.

마지막에 brr중 가장 큰 값을 출력한다.
