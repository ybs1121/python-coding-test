n = int(input())
dp = [0] * 101
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(4,n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])