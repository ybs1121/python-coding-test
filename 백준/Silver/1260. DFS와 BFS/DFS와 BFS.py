import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = {}

for i in range(n + 1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()


# DFS (깊이 탐색)

def dfs(start, visited):
    if visited[start]:
        return
    visited[start] = True

    print(start, end=" ")

    for node in graph[start]:
        dfs(node, visited)


dfs(v, [False] * (n + 1))
print()


# BFS

def bfs(start, visited):
    q = deque()
    q.append(start)
    while q:
        popleft = q.popleft()

        if visited[popleft]:
            continue

        visited[popleft] = True
        print(popleft, end=" ")
        for node in graph[popleft]:
            q.append(node)


bfs(v, [False] * (n + 1))
