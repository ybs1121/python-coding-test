from collections import deque

nx = [0, 1, 0, -1]
ny = [1, 0, -1, 0]


def dfs(x, y, graph, n, m):
    # 본인 방문처리
    graph[x][y] = 1

    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]

        if 0 <= dx < n and 0 <= dy < m and not graph[dx][dy]:
            dfs(dx, dy, graph, n, m)


def bfs(q, graph, n, m):
    while q:
        x, y = q.popleft()
        graph[x][y] = 1

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if 0 <= dx < n and 0 <= dy < m and not graph[dx][dy]:
                q.append((dx, dy))


n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append([int(char) for char in input()])

answer = 0

x, y = 0, 0

for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            answer += 1
            # 탐색하기
            # dfs(i, j, graph, n, m)
            q = deque()
            q.append((i,j))
            bfs(q, graph, n, m)


print(answer)

