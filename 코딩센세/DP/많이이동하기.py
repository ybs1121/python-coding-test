N = int(input())
graph = [list(map(int, input().split())) for _ in (N)]

dp = [[0 for _ in range(N)] for _ in range(N)]


# 모든 점을 방문한다.

# 방문한 뒤에 이동할 수 있는 모든 경우의 수를 재귀로 구현한다!

# 재귀로 구현한 뒤 DP

# def recur(y, x):
#     point = 0
#     for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#         ey = y + dy
#         ex = x + dx
#
#         if 0 <= ey < N and 0 <= ex < N:
#             if graph[y][x] < graph[ey][ex]:
#                 point = max(point, recur(ey, ex) + 1)
#
#         return point

def recur(y, x):
    if dp[y][x] != 0:
        return dp[x][y]

    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ey = y + dy
        ex = x + dx

        if 0 <= ey < N and 0 <= ex < N:
            if graph[y][x] < graph[ey][ex]:
                dp[y][x] = max(point, recur(ey, ex) + 1)

        return dp[y][x]


for y in range(N):
    for x in range(N):
        point = recur(y, x)
        print(point)

print(max(map(max, dp)) + 1)
