import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    T = int(input())

    dp = [0 for _ in range(T + 1)]


    for i in range(0, T + 1):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[T])
