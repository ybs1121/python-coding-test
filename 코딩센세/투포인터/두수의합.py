n = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.sort()
answer = 0
st = 0
ed = n - 1

while st < ed:
    if nums[st] + nums[ed] > target:
        ed -= 1
    elif nums[st] + nums[ed] < target:
        st += 1
    else:
        answer += 1
        # ed -= 1
        st += 1

print(answer)
