import sys
from collections import deque

input = sys.stdin.readline

N, M, H = map(int, input().split())

maps = []
for _ in range(H):
    line = []
    for _ in range(M):
        line.append(list(map(int, input().split())))
    maps.append(line)
# print(*maps, sep='\n')

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    flag = False
    q = deque()
    for z in range(H):
        for y in range(M):
            for x in range(N):
                if maps[z][y][x] == 1:
                    q.append((x, y, z))
                if maps[z][y][x] == 0:
                    flag = True
    if not flag:
        print(0)
        return

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                # print(nx, ny, nz)
                if maps[nz][ny][nx] == 0:
                    maps[nz][ny][nx] = maps[z][y][x] + 1
                    q.append((nx, ny, nz))

    answer = 0
    for z in range(H):
        for y in range(M):
            for x in range(N):
                if maps[z][y][x] == 0:
                    print(-1)
                    return
                answer = max(answer, maps[z][y][x])

    print(answer - 1)
    return


bfs()
