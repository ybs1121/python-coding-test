import sys

input = sys.stdin.readline

exp = input().rstrip().split("-")

nums = []

for i in exp:
    splits = i.split("+")
    temp = 0
    for split in splits:
        temp += int(split)
    nums.append(temp)

answer = nums[0]

for i in range(1, len(nums)):
    answer -= nums[i]

print(answer)
