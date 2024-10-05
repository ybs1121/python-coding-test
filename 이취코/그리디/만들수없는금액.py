# 5
# 3 2 1 1 9
from itertools import combinations

n = int(input())
nums = list(map(int,input().split()))

# val_array = [0] * 1_000_000_001
#
# for i in range(n):
#     for combo in combinations(nums,i):
#         idx = sum(combo)
#         val_array[idx] = 1
#
#
# for i in range(len(val_array)):
#     if val_array[i] == 0:
#         print(i)
#         break

nums.sort()
target = 1
for x in nums:
    if target < x:
        break
    target += x
print(target)
