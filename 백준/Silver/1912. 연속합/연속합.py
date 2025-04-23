import sys

n = int(input())
nums = list(map(int, input().split()))

dp = [-1001] * (n + 1)

dp[1] = nums[0]

idx = 1
compare_sum = nums[0]
for i in range(2, n+1):

    if 0 > compare_sum:
        compare_sum = nums[i - 1]
    else:
        compare_sum += nums[i - 1]

    dp[i] = max(dp[i - 1], compare_sum)

print(max(dp))
# print(dp)
