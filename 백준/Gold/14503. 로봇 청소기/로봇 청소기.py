import sys

input = sys.stdin.readline

N, M = map(int, input().split())

maps = []
robot_x, robot_y, way = map(int, input().split())

for i in range(N):
    maps.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 1
visited[robot_x][robot_y] = True

while True:
    idx = way
    flag = False

    for i in range(4):
        idx = (idx - 1) % 4
        nx = robot_x + dx[idx]
        ny = robot_y + dy[idx]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and maps[nx][ny] == 0:
                visited[nx][ny] = True
                answer += 1
                robot_x, robot_y, way = nx, ny, idx
                flag = True

                break

    if not flag:
        back = (way - 2) % 4
        nx = robot_x + dx[back]
        ny = robot_y + dy[back]

        if 0 <= nx < N and 0 <= ny < M:
            if maps[nx][ny] == 0:
                robot_x, robot_y = nx, ny


            else:
                break



print(answer)
