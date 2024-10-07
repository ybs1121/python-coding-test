# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4
from collections import deque

n, m, k, x = map(int, input().split())
maps = []
maps = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a not in maps:
        maps[a] = [[a, b, 0]]
    else:
        maps.get(a).append([a, b, 0])

visited = [False] * (n + 1)
INF = 1_000_000_001
min_val = [INF] * (n + 1)
for i in maps.keys():
    visited = [False] * (n + 1)
    pop = maps.get(i)

    q = deque(pop)
    while q:
        q_pop = q.popleft()
        a = q_pop[0]
        b = q_pop[1]
        cnt = q_pop[2]
        if not visited[b]:
            visited[b] = True
            cnt += 1
            min_val[b] = min(min_val[b], cnt)
            cities = maps.get(b)
            if cities != None:
                for city in cities:
                    city[2] = cnt
                    q.append(city)
print(min_val)
answer = []
for i in range(1,len(min_val)):
    if min_val[i] == k:
        answer.append(i)
if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)
