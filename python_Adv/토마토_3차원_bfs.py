# 문제 : https://www.acmicpc.net/problem/7569 
# 솔루션 : https://claude-u.tistory.com/273 / 
# 솔루션2 : https://dapsu-startup.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%86%A0%EB%A7%88%ED%86%A0-7569-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
# 익은 토마토 1 / 안익은 토마토 0  

""" 
1. DFS
- 재귀적인, 모든 경우를 하나씩 전부 탐색 
- Graph의 크기가 클 경우

2. BFS 
- 최단 거리 / 최단 횟수 
- BFS는 가장 처음 발견되는 해답이 최단 거리이다. 
- 탐색의 횟수
"""

from collections import deque 
from itertools import combinations 
import numpy as np

m, n, h = map(int, input().split())
graph = []

for k in range(h):
    list_h = []
    for i in range(n):
        temp = list(map(int, input().split()))
        list_h.append(temp)
    graph.append(list_h)

queue = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                queue.append((k, i, j))

print('queue', queue)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():

    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1 
                    queue.append((nz, nx, ny))

bfs()
day = 0
for k in graph:
    for i in k:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        max_value = max(i)
        day = max(day, max_value)

print(day-1)

            


