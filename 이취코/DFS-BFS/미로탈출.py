from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]


def bfs(x, y, count):
    q = deque()
    q.append((x, y,count))

    while q:
        qx, qy, qcount = q.popleft()

        if qx == n - 1 and qy == m - 1:
            return qcount

        for i in range(4):
            dx = qx + nx[i]
            dy = qy + ny[i]

            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy]:
                q.append((dx, dy, qcount + 1))


print(bfs(0, 0, 1))
