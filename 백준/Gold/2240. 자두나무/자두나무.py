import sys

# input = sys.stdin.readline().split
# T, W = map(int, input().split())
#
# data = []
# for _ in range(T):
#     data.append(int(input()))

# print(T, W)
# print(data)
#
# result = -1
#
#
# def catch(mv_cnt, sec, fruit_cnt, point):
#     global result
#     # print("호출 : " + str(sec))
#     if sec == T:
#         # print("호출")
#         result = max(result, fruit_cnt)
#         return None
#
#     if point == data[sec]:
#         fruit_cnt += 1
#
#     if mv_cnt < W:
#         if point == 1:
#             moving = 2
#         else:
#             moving = 1
#
#         catch(mv_cnt + 1, sec + 1, fruit_cnt, moving)
#
#     catch(mv_cnt, sec + 1, fruit_cnt, point)
#
#
#
#
# catch(0, 0, 0, 1)
#
# print(result)

T, W = map(int, input().split())
jadu = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]

# bottom_up dp
dp[1][0], dp[1][1] = jadu[1] % 2, jadu[1] // 2
for t in range(2, T + 1):
    for w in range(W + 1):
        j = jadu[t] % 2 if w % 2 == 0 else jadu[t] // 2
        dp[t][w] = max(dp[t - 1][0:w + 1]) + j
print(max(dp[-1]))
