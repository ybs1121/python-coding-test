import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

multi_box = []
for _ in range(H):
    boxs = []
    for _ in range(N):
        boxs.append(list(map(int, input().split())))
    multi_box.append(boxs)

nx = [1, -1, 0, 0, 0, 0]
ny = [0, 0, 1, -1, 0, 0]
nz = [0, 0, 0, 0, -1, 1]

visited = [[[False] * M for _ in range(N)] for _ in range(H)]

q = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if multi_box[z][y][x] == 1:
                q.append((x, y, z))


def dfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            dx = x + nx[i]
            dy = y + ny[i]
            dz = z + nz[i]

            if 0 <= dx < M and 0 <= dy < N and 0 <= dz < H:
                if multi_box[dz][dy][dx] == 0:
                    multi_box[dz][dy][dx] = multi_box[z][y][x] + 1
                    q.append((dx, dy, dz))


dfs()

answer = 0

for z in range(H):
    for y in range(N):
        for x in range(M):
            if multi_box[z][y][x] == 0:
                print(-1)
                exit(0)
            answer = max(answer, multi_box[z][y][x])

print(answer - 1)
