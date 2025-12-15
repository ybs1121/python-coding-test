import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# robot = list(map(int, input().split()))  # 0,1 : 좌표 2: 방향

x, y, way = map(int, input().split())

maps = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
    maps.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append([x, y, way])

answer = 1  # 초기 위치
visited[x][y] = True


while True:
    idx = way
    flag = False

    for i in range(4):
        idx = (idx - 1) % 4

        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < N and 0 <= ny < M:
            if maps[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                answer += 1
                x, y, way = nx, ny, idx
                flag = True
                break

    if not flag:
        back_idx = (way + 2) % 4
        nx = x + dx[back_idx]
        ny = y + dy[back_idx]

        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
            x, y = nx, ny
        else:
            break  # 뒤도 막혀있으면 종료

print(answer)


