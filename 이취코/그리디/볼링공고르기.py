# 315p
# 5 3
# 1 3 2 3 2
from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))
kinds = []
c = list(combinations(balls, 2))

for i in c:
    if i[0] != i[1]:
        kinds.append(i)

print(len(kinds))

