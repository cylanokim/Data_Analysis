# 가로 m / 세로 n
m, n = map(int, input().split())

# 토마토 받아서 넣기
# When you are not interested in some values returned by a function 
# we use underscore in place of variable name. Basically it means you are not 
# 
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 정답이 담길 변수 
res = 0 

# queue에 익은 사과의 위치를 넣는다.
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i,j])

print(matrix)

def bfs():
    while queue: # queue에 원소가 있는한....
        # 처음 토마토 좌표 x, y에 꺼내고
        x, y = queue.popleft()

        # 처음 토마토 주위의 익힐 토마토를 찾는다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1 
                queue.append([nx, ny])
                print(np.array(matrix))


bfs()
print(matrix)
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res-1)
