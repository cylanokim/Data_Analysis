from itertools import combinations 
import numpy as np

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
print(np.array(graph))

houses = []
chickes = []
result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i,j))
        elif graph[i][j] == 2:
            chickes.append((i,j))

# 
chickin_combos = list(combinations(chickes, m)) # -> m=2일 경우 (4,2), (4,3).....

# i에는 m개의 좌표가 담김. ex) (4,2), (2,3).... 총 m개
"""  
1. 먼저 m개의 치킨집 조합을 뽑는다.
2. 특정 치킨집 조합에서....
3. 집을 loop 한다.
4. 요 loop에서 집 하나와 조합에 있는 치킨집과의 거리를 구한다.
"""
for combo in chickin_combos:
    temp_dist = 0
    for house in houses:
        chickin_lengths = []
        for i in combo:
            chickin_lengths.append((abs(house[0]-i[0]) + abs(house[1]-i[1]))) 
        temp_dist += min(chickin_lengths)
    
    result = min(result, temp_dist)

print(result)

        
       
