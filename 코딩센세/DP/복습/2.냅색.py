A, B = map(int, input().split())

things = [list(map(int, input().split())) for _ in range(A)]

dp = [[-1 for _ in range(100)] for _ in range(A)]


def recur(idx, w):
    if w > B:  # idx == A 와 조건 순서가 바뀌면 무게를 넘어도 0으로 리턴하기 떄문에 문제 발생
        return -9999999
    if idx == A:
        return 0
    if dp[idx][w] != -1:
        return dp[idx][w]

    dp[idx][w] = max(recur(idx + 1, w + things[idx][0]) + things[idx][1], recur(idx + 1, w))
    return dp[idx][w]


recur(0, 0)
# print(dp[0][0])
print(dp)
max_val = max(max(row) for row in dp)
print(max_val)

# 4 7
# 6 13
# 4 8
# 3 6
# 5 12


A, B = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(A)]  # (w, v)

NEG_INF = -10 ** 15
dp = [[None] * (B + 1) for _ in range(A + 1)]


def recur(idx, w):
    if w > B:
        return NEG_INF
    if idx == A:
        return 0
    if dp[idx][w] is not None:
        return dp[idx][w]
    take = recur(idx + 1, w + things[idx][0]) + things[idx][1]
    skip = recur(idx + 1, w)
    dp[idx][w] = max(take, skip)
    return dp[idx][w]


print(recur(0, 0))
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
items = []
# y축 = 물건의 무게, 가치  / x축 = 배낭의 무게
# +1 달아서 0,0은 0으로 추가 (물건을 못넣을 때)
dp = [[0] * (k + 1) for _ in range(n + 1)]

for y in range(1, n + 1):  # 물건이
    weight, value = map(int, input().split())
    for x in range(1, k + 1):  # 가방 무게가 x일 때
        # 물건을 담을 수 있을 때 (x보다  무게가 작거나 같을 때)
        if x < weight:
            dp[y][x] = dp[y - 1][x]

        # 물건을 담을 수 없을 때 ( 전에 넣어뒀던 무게로 유지)
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - weight] + value)

print(dp[n][k])
