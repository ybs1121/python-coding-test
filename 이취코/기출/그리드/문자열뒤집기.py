nums = list(map(int, input()))


count_zero = 0
count_one = 0


standard = nums[0]

for i in range(len(nums)):
    if standard == nums[i]:
        continue
    else:
        if standard == 0:
            count_zero += 1
        else:
            count_one += 1

        standard = nums[i]


print(min(count_one, count_zero))