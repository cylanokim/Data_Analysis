import numpy as np
from copy import deepcopy
n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt_3 = 0

print(np.array(graph))

def dfs(x, y):
    
    current_color = graph[x][y]
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] == current_color:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt_3 += 1
##################################################
# 적록 R -> G
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

cnt_2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt_2 += 1

print(f'#{cnt_3} {cnt_2}')
