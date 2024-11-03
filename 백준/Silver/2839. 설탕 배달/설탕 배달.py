import sys

n = int(input())

dp = [sys.maxsize] * (n + 1)
dp[n] = 0

for i in range(n, -1, -1):

    if i - 3 > -1:
        dp[i - 3] = min(dp[i - 3], dp[i] + 1)
    if i - 5 > -1:
        dp[i - 5] = min(dp[i - 5], dp[i] + 1)

if dp[0] == sys.maxsize:
    print(-1)
else:
    print(dp[0])