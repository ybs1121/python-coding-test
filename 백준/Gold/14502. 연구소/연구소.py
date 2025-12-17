import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maps = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
    maps.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

MAX_WALL = 3

answer = 0

empty_spaces = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            empty_spaces.append((i, j))


def find(cnt):
    global answer

    if cnt == MAX_WALL:
        # 바이러스를 경로 돌고
        # answer 업데이트
        tmp_map = [row[:] for row in maps]
        answer = max(bfs(tmp_map), answer)
        return

    for walls in combinations(empty_spaces, 3):
        tmp_maps = [row[:] for row in maps]

        # 벽 세우기
        for r, c in walls:
            tmp_maps[r][c] = 1

        answer = max(answer, bfs(tmp_maps))


def bfs(maps):
    q = deque()

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                q.append((i, j))

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 0:
                    q.append((nx, ny))
                    maps[nx][ny] = 2

    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                cnt += 1

    return cnt


find(0)

print(answer)
