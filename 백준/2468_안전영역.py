import sys
sys.setrecursionlimit(100000)

N = int(input())
maps = []
max_h = -1
for i in range(N):
    l = list(map(int, input().split()))
    maps.append(l)
    temp_max_h = max(l)
    max_h = max(temp_max_h, max_h)

nx = [0, 1, -1, 0]
ny = [1, 0, 0, -1]

visit = [[False] * N for _ in range(N)]


def dfs(x, y, rain):
    if maps[x][y] > rain and visit[x][y] == False:
        visit[x][y] = True
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0 <= dx < N and 0 <= dy < N and rain < maps[dx][dy]:
                dfs(dx, dy, rain)
        return True
    else:
        return False


result = -1
for rain in range(max_h):
    visit = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if dfs(i, j, rain):
                count += 1
    result = max(result, count)

print(result)
