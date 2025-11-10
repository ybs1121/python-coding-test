import sys

sys.setrecursionlimit(100000)  # 원하는 깊이만큼 설정

input = sys.stdin.readline
r, c = map(int, input().split())

maps = []
for i in range(r):
    maps.append(input().rstrip())

answer = 0

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

visited = [0] * 26
max_depth = 0


def dfs(i, j, depth):
    global max_depth

    if max_depth < depth:
        max_depth = depth

    for n in range(4):
        dx = nx[n] + i
        dy = ny[n] + j
        if 0 <= dx < r and 0 <= dy < c and visited[ord(maps[dx][dy]) - 65] != 1:
            visited[ord(maps[dx][dy]) - 65] = 1
            dfs(dx, dy, depth + 1)
            visited[ord(maps[dx][dy]) - 65] = 0


visited[ord(maps[0][0]) - 65] = 1
dfs(0, 0, 1)
print(max_depth)
