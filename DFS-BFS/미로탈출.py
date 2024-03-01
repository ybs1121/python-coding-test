from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111


result = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x = 0
y = 0
# deque = deque([(0, 0)])


def bfs():
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if x + 1 == n and y + 1 == m:
            return True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1


bfs()

print(maps)
print(maps[n-1][m-1])
