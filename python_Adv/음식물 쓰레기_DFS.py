# https://www.acmicpc.net/problem/1743
# 솔루션 : https://soopeach.tistory.com/18

import sys 
sys.setrecursionlimit(10**7)
import numpy as np 

def dfs(r, c):
    global size
    if r <= -1 or r >= n or c <= -1 or c >= m:
        return False 
    
    if graph[r][c] == 1:
        size += 1
        graph[r][c] = 0

        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c+1)
        dfs(r, c-1)
        return True

    return False


# n: 세로, m: 가로, k:쓰레기 개수
n, m, k = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*m for _ in range(n)]

size = 0 
ans = 0

for i in range(k):
    r, c = map(int, sys.stdin.readline().rstrip().split()) # .split()을 추가하면 space를 누른 단위로 입력된다.
    graph[r-1][c-1] = 1

print(np.array(graph))

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            ans = max(size, ans)
            size = 0

print(ans)

