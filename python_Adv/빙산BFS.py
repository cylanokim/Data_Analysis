# https://www.acmicpc.net/problem/2573
# 솔루션 : https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2573-%EB%B9%99%EC%82%B0-BFS
# 솔루션 : https://fre2-dom.tistory.com/499
import sys 
from collections import deque 
import numpy as np

def bfs(a, b):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([[a,b]])
    visited[a][b] = True 

    while queue:
        # queue에서 기존 빙산을 제거하고 주위를 탐색. 만약 주변에 빙산이 이어져 있으면 그 새로운 빙산을
        # queue에 다시 추가하여 while문을 반복!!!
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고 탐색하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 빙산이라면 큐에 추가 
                if graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                
                # 빙산이 아니라면 바닷물로 카운트
                else:
                    cnt[x][y] += 1
    return 1

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
year = 0

print(np.array(graph))

while True:
    print('while begins-----------------')
    answer = []
    visited = [[False]*m for _ in range(n)]
    cnt = [[0]*m for _ in range(n)]

    # 빙산과 접촉되어 있는 바닷물 확인
    for i in range(n):
        for j in range(m):
            # 아직 방문하지 않은 빙산이라면!!
            if graph[i][j] != 0 and not visited[i][j]:
                answer.append(bfs(i,j))

    # 빙산을 깎아 줌
    for i in range(n):
        for j in range(m):
            graph[i][j] -= cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    if len(answer) == 0 or len(answer) >= 2:
        break
    
    print('graph', np.array(graph))
    print('visited', np.array(visited))
    print('cnt', np.array(cnt))
    year += 1
    print(answer)
    print('while ends-----------------')

print(year) if len(answer) >= 2 else print(0)



