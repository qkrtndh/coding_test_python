<h1>11725</h1>

![image](https://user-images.githubusercontent.com/65153512/120912312-059f8a80-c6c9-11eb-8b6f-c2e2191deddd.png)

입력받은 정보들은 그래프의 edge 정보와 같다.

이 정보를 토대로 각 노드들에 간선정보(도착 노드)를 저장한다.

루트노드를 1로 두었다고 할때, 1에서 출발하는 그래프가 완성된다.

1번 노드부터 dfs를 통해 모든 노드들을 방문하면서 자식 노드가 있는 경우 해당 자식노드 번호의 리스트에 자신의 번호를 설정한다.
이 설정한 번호는 해당 노드의 부모라는 표시가 되고, dfs가 끝나면 1번노드를 제외한 모든 노드들의 부모노드들이 표시된다.