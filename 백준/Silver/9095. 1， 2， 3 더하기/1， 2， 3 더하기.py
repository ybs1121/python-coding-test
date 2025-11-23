import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())

    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n])

