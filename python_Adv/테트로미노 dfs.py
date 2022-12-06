# https://www.acmicpc.net/problem/14500
# sol https://esoongan.tistory.com/187
# sol https://pottatt0.tistory.com/entry/%EB%B0%B1%EC%A4%80-14500-%ED%95%B4%EC%84%A4-python-%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8
import numpy as np


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x, y, L, total):
    global result
    visited[x][y] = True

    if L == 4:
        result = max(result, total)
        return 
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if L == 2:
                    dfs(nx, ny, L+1, total + graph[nx][ny])
                    visited[nx][ny]
                dfs(nx, ny, L+1, total + graph[nx][ny])
                visited[nx][ny] = False

# 준비
result = 0
max_val = max(map(max, graph))

for i in range(n):
    for j in range(m):
        dfs(i, j, 1, graph[i][j]) 
        graph[i][j] = False

print(result)
