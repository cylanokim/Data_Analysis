""" 
1. DFS
- 음료수 얼려먹기, 유기농 배추, 바이러스, 달리기, 감시, 쓰레기
- 재귀 함수
- 함수 모양 : 1. 범위
- 격자 map이 있는 경우 -> for문을 돌리며 dfs 함수를 실행한다.
- 격자 map이 없는 경우 (ex:네트워크) -> dfs 함수 내에서 for문을 돌린다.
- 

2. BFS
- from collecitons import deque
- while queue: 를 거의 사용
- for i in range(4): -> 요 아래에서 알고리즘이 돌아가야함
- queue 변수 입력
    경우 1: queue에 원소를 하나만 담고, 계속 바꿔가다가 원소가 사라지면 while
    을 나가게 하는 경우는 queue.append((x,y))

    경우 2: queue에 원소를 계속 넣어가는 경우에는 (ex:빙산)
    queue.append([(x,y)])

3. 공통
- import copy
  graph_copy = copy.deepcopy(graph)

""" 
import sys 
from collections import deque 
import numpy as np
sys.setrecursionlimit(10*7)

def dfs(r, c, level):
    if r <= -1 or r >= n or c <= -1 or c >= n:
        return False 
    
    # 수면 보다 높고 visited 하지 않으면 (처음 방문하면)
    if graph[r][c] > level and not visited[r][c]:
        visited[r][c] = True
        print('bfs here')
        
        dfs(r-1, c, level)
        dfs(r+1, c, level)
        dfs(r, c-1, level)
        dfs(r, c+1, level)
        return True 
    return False


n = int(input())
max_num = 0
result = 1
# graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(temp)

    for j in temp:
        if j > max_num:
            max_num = j

print(np.array(graph))

cnt_list = []

for level in range(max_num):

    cnt = 0
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # if graph[i][j] > level and not visited[i][j]:
            if dfs(i, j, level):
                cnt +=1 

    cnt_list.append(cnt)
    result = max(result, cnt)

print(cnt_list)
print(result)
