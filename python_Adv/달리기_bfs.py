""" 
1. DFS
- 음료수 얼려먹기, 유기농 배추, 바이러스, 달리기
- 재귀 함수
- 함수 모양 : 1. 범위
- 격자 map이 있는 경우 -> for문을 돌리며 dfs 함수를 실행한다.
- 격자 map이 없는 경우 (ex:네트워크) -> dfs 함수 내에서 for문을 돌린다.

2. BFS
- from collecitons import deque
- while queue: 를 거의 사용
- for i in range(4): -> 요 아래에서 알고리즘이 돌아가야함

""" 

import sys 
from collections import deque 
import numpy as np 

def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1))

    graph[x1][y1] = 0
    # visited[x1][y1] = True

    while queue:
        x, y = queue.popleft()

        if (x == x2) and (y == y2):
            return graph[x2][y2]
        for i in range(4):
            for j in range(1, k+1):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
            
            # 범위 밖이면 다음 방향 탐색
                if nx < 0 or nx >=n or ny < 0 or ny >= m:
                    break 
                if graph[nx][ny] == '#':
                    break 
                if graph[nx][ny] == '.':
                    print('here')
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
                if graph[nx][ny] > graph[x][y]:
                    continue
                else:
                    break
    return -1



input = sys.stdin.readline
# 세로, 가로, 1초에 이동가능한 최대 칸
n, m, k = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(n)] # .split()을 x -> 입력된대로 list가 생성 
visited = [[False]*m for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split()) # space bar로 입력됨

print(np.array(graph))
print('x1, y1, x2, y2 : ', x1, y1, x2, y2)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(x1-1, y1-1, x2-1, y2-1))
print(np.array(graph))
