# 1753
from collections import deque
import heapq

N, M = map(int, input().split())
start = int(input())
links = [[] for _ in range(N + 1)]
dist = [1e9 for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    links[A].append([B, C])

# BFS

q = []
q.append([0, start])
heapq.heappush(q, [0, start])
dist[start] = 0

# def shortest_finder():
#     mini = 1e9
#     idxs = 0
#     for i in range(1, N + 1):
#         if dist[i] <= mini:
#             idxs = i
#             mini = dist[i]
#     return idxs
#

while q:
    # 우선순위 큐 이용
    heapq.heapify(q)
    _w, node = heapq.heappop(q)
    for nxt, weight in links[node]:
        # 1 각각의 노드에 값을 업데이트
        #     # 2. 만약 여러 경로가 있다면 min 비교
        #     # 3. 시적점으로 거리를 봐서, 짧은 순서대로 안그러면 오염
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q, [dist[nxt], nxt])
        # idx = shortest_finder()
        # if idx in q:
        #     q.remove(idx)
        #     q.appendleft(idx)

        print(dist)
