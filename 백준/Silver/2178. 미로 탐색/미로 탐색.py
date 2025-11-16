import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maps = []
for _ in range(N):
    line = list(map(int, input().rstrip()))
    maps.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# visited = [[False for _ in range(M)] for _ in range(N)]


def dfs(target_x, target_y):
    q = deque([(0, 0)])
    # print(target_x, target_y)
    # print("=")
    while q:
        x, y = q.popleft()
        # print(x, y)

        if x == target_x and y == target_y:
            return maps[x][y]

        # if visited[x][y]:
        #     continue

        # visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    return -1


print(dfs(N - 1, M - 1))
