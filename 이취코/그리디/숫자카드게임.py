n, m = map(int, input().split())

answer = 0

for i in range(n):
    nums = list(map(int, input().split()))

    min_val = min(nums)

    answer = max(answer, min_val)

print(answer)

