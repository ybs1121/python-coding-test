ny, nx = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(ny)]
dp = [[-1 for _ in range(nx)] for _ in range(ny)]


def recur(y, x):
    if ny - 1 == y and nx - 1 == x:
        return 1

    if dp[y][x] != 0:
        return dp[y][x]

    route = 0
    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ex = x + dx
        ey = y + dy
        if 0 <= ex < nx and 0 <= ey < ny:
            if graph[ey][ex] < graph[y][x]:
                route += recur(ey, ex)
    dp[y][x] = route
    return dp[y][x]


recur(0, 0)
print(recur(0, 0))
