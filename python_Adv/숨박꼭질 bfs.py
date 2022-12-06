# https://www.acmicpc.net/problem/1697
# https://great-park.tistory.com/19

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
N = 5 
K = 17 

graph = [0] * (10000)

def bfs(N, K):
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:
            return
        
        for i in (x-1, x+1, 2*x):
            if graph[i] == 0 : # and 0 <= i < 10001
                graph[i] = graph[x] + 1
                queue.append(i)

bfs(N, K)
print(graph[K])
print(graph[:K+1])
