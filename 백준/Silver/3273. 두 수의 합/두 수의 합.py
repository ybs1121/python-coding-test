import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

st = 0
ed = len(nums) - 1

nums.sort()
answer = 0
while st < ed:
    a = nums[st] + nums[ed]

    if a > x:
        ed -= 1
    elif a < x:
        st += 1
    else:
        answer += 1
        st += 1
        ed -= 1

print(answer)