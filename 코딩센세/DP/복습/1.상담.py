N = int(input())

sch = [list(map(int, input().split())) for _ in range(N)]

dp = [-1 for _ in range(N + 1)]


def recur(idx):
    if idx == N - 1:
        return 0
    if idx >= N:
        return -999999999999

    if dp[idx] != -1:
        return dp[idx]

    dp[idx] = max(recur(idx + sch[idx][0]) + sch[idx][1], recur(idx + 1))

    return dp[idx]


for i in range(N, 1, -1):
    # 상담을 받거나 안받거나

    max(dp[i], dp[i] + dp[i - 1])

recur(0)
print(dp)

dp = [-1 for _ in range(N + 1)]

for idx in range(N + 1)[::-1]:
    if idx + sch[idx][0] > N:
        dp[idx] = dp[idx + 1] # 범위를 벗어남

    dp[idx] = max(dp[idx + sch[idx][0]] + sch[idx][1], dp[idx + 1])
