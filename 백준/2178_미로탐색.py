from collections import deque

N, M = map(int, input().split())  # 미로의 크기 입력
maze = [list(map(int, input())) for _ in range(N)]  # 미로 입력


def bfs(maze, N, M):
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0)])  # 시작 지점 (1, 1)
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우 이동
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1  # 이동 거리 기록
    return maze[N - 1][M - 1]  # 도착 지점까지의 최소 이동 거리 반환

print(bfs(maze, N, M))  # 최소 이동 거리 출력
