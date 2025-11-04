import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())


graph = {i: [] for i in range(1, N + 1)}
for M in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()


dfs_visited = [False] * (N + 1)


def dfs(node, visited):
    if visited[node]:
        return

    visited[node] = True
    print(node, end=" ")

    for neighbor in graph[node]:
        dfs(neighbor, visited)


dfs(V, dfs_visited)

print()
q = deque([V])

bfs_visited = [False] * (N + 1)

while q:
    node = q.popleft()

    if bfs_visited[node]:
        continue

    print(node, end=" ")

    bfs_visited[node] = True

    for neighbor in graph[node]:
        q.append(neighbor)

