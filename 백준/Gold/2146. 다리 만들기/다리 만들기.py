import sys
from collections import deque

answer = sys.maxsize
n = int(input())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
redraw_visited = [[False] * n for _ in range(n)]

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

# 대륙간 구분을 만든다?

idx = 0
for x in range(n):
    for y in range(n):
        if maps[x][y] == 1 and redraw_visited[x][y] == False:
            q = deque()
            q.append((x, y))
            idx += 1
            redraw_visited[x][y] = True
            maps[x][y] = idx

            while q:
                x, y = q.popleft()

                for i in range(4):
                    dx = x + nx[i]
                    dy = y + ny[i]
                    if 0 <= dx < n and 0 <= dy < n and maps[dx][dy] == 1 and redraw_visited[dx][dy] == False:
                        q.append((dx, dy))
                        maps[dx][dy] = idx
                        redraw_visited[dx][dy] = True



def find(island):
    q = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == island:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            dx = nx[i] + x
            dy = ny[i] + y
            if 0 <= dx < n and 0 <= dy < n:
                if maps[dx][dy] != island and maps[dx][dy] != 0:
                    return dist[x][y]
                if maps[dx][dy] == 0 and dist[dx][dy] == -1:
                    dist[dx][dy] = dist[x][y] + 1
                    q.append((dx, dy))


for island in range(1, idx + 1):
    answer = min(answer, find(island))

print(answer)
