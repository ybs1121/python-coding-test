import math

# n = int(input())
#
## 가장 큰수를 빼면서 하면 되지 않을까?
# sq = math.sqrt(n)
#
# count = 0
# if sq % 1 == 0:
#     # print("한번에")
#     print(1)
#
# else:
#     while n > 0:
#         count += 1
#         sq = sq // 1
#         # print("뺀 제곱근" +str(sq))
#         n -= (sq*sq)
#         # print(n)
#         sq = math.sqrt(n)
#         # print("새로 제곱근" +str(sq))
#
#
#     print(count)


n = int(input())
dp = [x for x in range (n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i :
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1
print(dp[n])