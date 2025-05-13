# 1520

import sys

# 재귀 한도 늘리기 (예: 3000)
sys.setrecursionlimit(99999999)

X, Y = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(X)]

answer = 0

dp = [[-1 for _ in range(Y)] for _ in range(X)]


# def recur(x, y):
#     global answer
#
#     if x == X - 1 and y == Y - 1:
#         answer += 1
#
#     for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#         ey = y + dy
#         ex = x + dx
#
#         if 0 <= ex < X and 0 <= ey < Y:
#             if graph[x][y] > graph[ex][ey]:
#                 recur(ex, ey)

def recur(x, y):
    if x == X - 1 and y == Y - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]
    route = 0



    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ey = y + dy
        ex = x + dx

        if 0 <= ex < X and 0 <= ey < Y:
            if graph[x][y] > graph[ex][ey]:
                route += recur(ex, ey)
    dp[x][y] = route
    return dp[x][y]

recur(0, 0)

# print(answer)

print(dp)