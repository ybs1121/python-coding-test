import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maps = []
for i in range(n):
    line = input().rstrip()
    maps.append([int(ch) for ch in line])

q = deque()
q.append((0, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()

    if maps[x][y] == 0:
        continue

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
            maps[nx][ny] = maps[x][y] + 1
            q.append((nx, ny))

print(maps[n - 1][m - 1])
