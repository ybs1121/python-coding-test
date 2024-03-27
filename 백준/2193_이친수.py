n = int(input())

# 이진수 범위
# 끝은 1 * N
min_binary = '1' + '0' * (n - 1)
min_binary = int('0b' + min_binary, 2)
max_binary = '1' * n
max_binary = int('0b' + max_binary, 2)
# print(min_binary)
# print(max_binary)
# result = 0
# for i in range(min_binary, max_binary + 1):
#     binary = bin(i)
#     binary = binary[2:]
#     for j in range(len(binary) - 1):
#         flag = False
#         if j == 0:
#             if binary[j] == '0':
#                 flag = True
#                 break
#         if binary[j] == binary[j + 1] and binary[j] == '1':
#             flag = True
#             break
#
#     if not flag:
#         result += 1
#
# print(result)


dp = [0] * 101
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(4,n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

# print(dp)
print(dp[n])