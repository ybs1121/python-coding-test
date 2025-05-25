# 2606
from collections import deque

n = int(input())
l = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(l):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n + 1)]

visited[1] = True
#
#
# def recur(node):
#     visited[node] = 1
#
#     for nxt in graph[node]:
#         if visited[nxt] == 1:
#             continue
#         else:
#             recur(nxt)
#
#
# recur(1)
# print(sum(visited) - 1)

q = deque()
q.append(1)

while q:
    nxt = q.popleft()
    visited[nxt] = 1
    for i in graph[nxt]:
        if visited[i] == 1:
            continue
        else:
            q.append(i)
print(visited)
print(sum(visited) - 1)