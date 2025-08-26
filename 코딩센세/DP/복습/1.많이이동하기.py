def recur(y, x):
    if dp[y][x] != 0:
        return dp[y][x]
    for dy, dx in [[0, 1], [0, -1],[1, 0],[-1, 0]]:
        ey = y + dy
        ex = x + dx

        if 0 <= ey < n and 0 <= ex < n:
            if graph[y][x] < graph[ey][ex]:
                dp[y][x] = max(dp[y][x], recur(ey, ex) + 1)

    return dp[y][x]

    # return max(recur(y - 1, x), recur(y + 1, x), recur(y, x - 1), recur(y, x + 1))


n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

# 모든 점을 방문한다.

# 방문한 뒤에 이동할 수 있는 모든 경우의 수를 재귀로 구현

# DP로 변경

for y in range(n):
    for x in range(n):
        point = recur(y, x)
        print(y, x, point)

print(max(map(max, graph)) + 1)
