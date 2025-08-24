n = int(input())

house = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]

for i in range(1, n):
    dp[i][0] = min(house[i][0] + dp[i - 1][1], house[i][0] + dp[i - 1][2])
    dp[i][1] = min(house[i][1] + dp[i - 1][0], house[i][0] + dp[i - 1][2])
    dp[i][2] = min(house[i][2] + dp[i - 1][0], house[i][0] + dp[i - 1][1])


print(dp)
