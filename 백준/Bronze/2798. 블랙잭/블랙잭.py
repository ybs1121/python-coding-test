import itertools


n, s = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

combinations = itertools.combinations(nums, 3)
answer = 0
for combination in combinations:
    i = sum(combination)
    if i > s:
        continue
    if s - i < s - answer:
        answer = i

print(answer)
