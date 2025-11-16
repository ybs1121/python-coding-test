import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

maps = []
for i in range(R):
    maps.append(list(map(str, input().rstrip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

dist = []
for i in range(R):
    dist.append([-1] * C)

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'S':
            q.append((i, j))
            dist[i][j] = 0
        elif maps[i][j] == '*':
            q.appendleft((i, j))

def dfs():
    while q:
        x, y = q.popleft()

        now = maps[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if dist[nx][ny] != -1:
                    continue

                if maps[nx][ny] == '*':
                    continue

                if maps[nx][ny] == 'X':
                    continue

                if now == '*' and maps[nx][ny] == 'D':
                    continue

                if now == 'S':
                    if maps[nx][ny] == 'D':
                        print(dist[x][y] + 1)
                        return
                    dist[nx][ny] = dist[x][y] + 1

                maps[nx][ny] = now
                q.append((nx, ny))

    print("KAKTUS")

dfs()

