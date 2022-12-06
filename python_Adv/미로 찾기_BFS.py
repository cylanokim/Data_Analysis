import sys 
from collections import deque  
import numpy as np


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    """  
    경우 1: queue에 원소를 하나만 담고, 계속 바꿔가다가 원소가 사라지면 while
    을 나가게 하는 경우는 queue.append((x,y))

    경우 2: queue에 원소를 계속 넣어가는 경우에는 (ex:빙산)
    queue.append([(x,y)])
    """  
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 

            # 공간을 벗어난 경우 or 공간일 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]

n, m = map(int, sys.stdin.readline().rstrip())
# graph = [list(map(int, input())) for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# # visited = [[0]*n for _ in range(m)] 이 필요한지 확인!!!
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

print(np.array(graph))
print(bfs(0,0))
print(np.array(graph))

