import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maps = []

for i in range(N):
    maps.append(list(map(int, input().split())))

max_wall = 3

answer = 0

blanks = []
virus = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            blanks.append([i, j])
        if maps[i][j] == 2:
            virus.append([i, j])


def counter(maps):
    global N, M

    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                cnt += 1

    return cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def finder():
    global answer

    for walls in combinations(blanks, max_wall):
        copy_map = []

        for i in range(N):
            copy_map.append(maps[i] + [])

        for wall in walls:
            copy_map[wall[0]][wall[1]] = 1

        # 전이
        q = deque(virus)

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if copy_map[nx][ny] == 0:
                        copy_map[nx][ny] = 2
                        q.append((nx, ny))

        answer = max(counter(copy_map), answer)


finder()

print(answer)
