# 1816


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

for num in nums:
    for i in range(2, 1_000_001):
        if num % i == 0:
            print("NO")
            break
        if i == 1_000_000:
            print("YES")
