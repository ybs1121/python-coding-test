# 14501 (탑다운)

N = int(input())

counsels = [list(map(int, input().split())) for _ in range(N)]

dp = [-1 for _ in range(N + 1)]


def recur(idx):
    global answer

    if idx == N - 1:
        return 0
    if idx >= N:
        return -999999999999

    if dp[idx] != -1:
        return dp[idx]

    dp[idx] = max(recur(idx + counsels[idx][0]) + counsels[idx][1], recur(idx + 1))

    return dp[idx]


recur(0)
print(dp)

dp = [0 for _ in range(N + 1)]

for idx in range(N + 1)[::-1]:
    if idx + counsels[idx][0] > N:
        dp[idx] = dp[idx + 1]
    else:
        dp[idx] = max(dp[idx + counsels[idx][0]] + counsels[idx][1], dp[idx + 1])
