import numpy as np
from collections import deque 

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
cnt = 0 

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

print(np.array(graph))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True 

    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i] 

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True 
                    queue.append((nx, ny))

for i in range(n): 
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            cnt +=1

print(cnt)
print(np.array(graph))
