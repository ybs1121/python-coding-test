import sys

input = sys.stdin.readline

n = int(input())

wine = []
for i in range(n):
    wine.append(int(input()))

dp = [0 for _ in range(n + 1)]
dp[0] = 0

for i in range(1, n + 1):
    if i == 1:
        dp[i] = wine[i - 1]
    elif i == 2:
        dp[i] = wine[i - 1] + dp[i - 1]
    else:
        dp[i] = max(dp[i - 1],  # 먹을 지 않았을 때
                    wine[i - 1] + dp[i - 2],
                    wine[i - 1] + wine[i - 2] + dp[i - 3])
print(dp[n])
