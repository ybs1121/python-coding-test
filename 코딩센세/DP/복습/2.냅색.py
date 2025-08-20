A, B = map(int, input().split())

things = [list(map(int, input().split())) for _ in range(A)]

dp = [[-1 for _ in range(100)] for _ in range(A)]


def recur(idx, w):
    if w > B: # idx == A 와 조건 순서가 바뀌면 무게를 넘어도 0으로 리턴하기 떄문에 문제 발생
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


print(recur(0, 0))  # ← 이 값이 14가 됩니다.
