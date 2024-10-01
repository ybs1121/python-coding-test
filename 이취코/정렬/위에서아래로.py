n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))

nums.sort(reverse=True)

for n in nums:
    print(n, end=' ')
