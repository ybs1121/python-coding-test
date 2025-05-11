# 12865 탑다운

def recur(cur, w):
    global ans
    if w > m:
        return -9999999

    if cur == n:
        return 0

    if dp[cur][w] != -1:
        return dp[cur][w]

    dp[cur][w] = max(recur(cur + 1, w + arr[cur][0]) + arr[cur][1], recur(cur + 1, w))

    return dp[cur][w]


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dp = [[-1 for _ in range(100010)] for j in range(n)]

ans = recur(0, 0)

print(ans)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for y in range(1, n + 1):  # 물건이
    weight, value = map(int, input().split())
    for x in range(1, m + 1):  # 가방 무게가 x일 때
        # 물건을 담을 수 있을 때 (x보다  무게가 작거나 같을 때)
        if x < weight:
            dp[y][x] = dp[y - 1][x]

        # 물건을 담을 수 없을 때 ( 전에 넣어뒀던 무게로 유지)
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - weight] + value)

print(dp[n][m])
