import sys
input = sys.stdin.readline
trees = {}#key:value로 저장
cnt = 0
 
while True:
    tree = input().strip() #enter 제외 입력값
    if not tree: #null인 경우
        break #빠져나옴
    #null이 아닌 경우
    trees.setdefault(tree, 0) #key=tree : value=0 로 초기화, 있다면 초기화 x
    trees[tree] += 1 #value에 1추가
    cnt += 1#총 수에 1 추가
 
for tree in sorted(trees.keys()):# 나무 이름 기준으로 나무들을 정렬
    print('{0} {1:0.4f}'.format(tree, trees[tree]*100/cnt))
    #0번째 값, 1번째값. 형식지정(tree는 키값(정렬기준), trees에서 tree를 키로하는 값의 100분율)