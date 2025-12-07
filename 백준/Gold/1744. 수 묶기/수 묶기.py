import sys

input = sys.stdin.readline

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

# 두 짝이 양수면 곱하고
# 두 짝이 음수면 곱하고
# 하나가 1이면 더하고
# 음수 * 0 이면 곱하고

negative = []
positive = []

for num in nums:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

negative_sum = 0
positive_sum = 0

positive.sort(reverse=True)
negative.sort()

for i in range(0, len(negative), 2):
    if i + 1 >= len(negative):
        negative_sum += negative[i]
    else:
        negative_sum += (negative[i] * negative[i + 1])

for i in range(0, len(positive), 2):
    if i + 1 >= len(positive):
        positive_sum += positive[i]
    else:
        if positive[i] == 1 or positive[i + 1] == 1:
            positive_sum += (positive[i] + positive[i + 1])
        else:
            positive_sum += (positive[i] * positive[i + 1])


print(positive_sum + negative_sum)
