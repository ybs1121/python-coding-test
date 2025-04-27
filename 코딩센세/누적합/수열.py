# 2559
import sys

a, b = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0 for _ in range(a + 1)]

for i in range(a):
    prefix[i + 1] = prefix[i] + nums[i]

answer = []
print(answer)

for i in range(b, a + 1):
    answer.append(prefix[i] - prefix[i - b])

print(max(answer))
