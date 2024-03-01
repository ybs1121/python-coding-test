n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
# visited = [[False for _ in range(m)] for _ in range(n)]

result = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x = 0
y = 0


def dfs(x, y):
    if maps[x][y] == 1:
        return False

    else:
        maps[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 0:
                maps[nx][ny] = 1
                x = nx
                y = ny
                dfs(x, y)

    return True


for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
        print(maps)

print("---")
print(maps)
print(result)
