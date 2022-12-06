import sys 
sys.setrecursionlimit(10**7)
import numpy as np  

def dfs(r, c):
    if r <= -1 or r > n or c <= -1 or c > m:
        return False 

    if graph[r][c] == 1:
        print('dfs here')

        graph[r][c] = 0 
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
        return True 
    
    return False

n, m, k = map(int, sys.stdin.readline().rstrip().split()) 
graph = [[0]*(m+1) for _ in range(n+1)]
cnt = 0

for _ in range(k):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    graph[r][c] = 1 

print(np.array(graph))

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1

print(np.array(graph))
print('cnt : ', cnt)
