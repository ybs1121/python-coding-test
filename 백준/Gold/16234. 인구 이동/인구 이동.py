import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))

answer = 0

nx = [0, 1, -1, 0]
ny = [1, 0, 0, -1]


def bfs(x, y):
    q = deque()

    q.append((x, y))

    summery = [(x, y)]

    while q:
        x, y = q.popleft()
        

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy]:
                if l <= abs(maps[dx][dy] - maps[x][y]) <= r:
                    visited[dx][dy] = True
                    q.append((dx, dy))
                    summery.append((dx, dy))

    return summery


while True:
    flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                summery = bfs(i, j)

                if len(summery) > 1:
                    flag = True
                    population = sum(maps[i][j] for i, j in summery) // len(summery)
        
                    for x, y in summery:
                        maps[x][y] = population

    if not flag:
        break

    answer += 1
print(answer)
