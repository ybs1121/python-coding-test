from collections import deque

import sys

input = sys.stdin.readline

n = int(input())
maps = []
for i in range(n):
    maps.append(input().rstrip())

visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

towns = []
for i in range(n):
    for j in range(n):

        if not visited[i][j] and maps[i][j] == '1':
            cnt = 0
            q = deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()
                if visited[x][y]:
                    continue

                visited[x][y] = True
                cnt += 1
                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y

                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[nx][ny] and maps[nx][ny] == '1':
                            q.append((nx, ny))

            if cnt > 0 :
                towns.append(cnt)

print(len(towns))
for x in sorted(towns):
    print(x)
