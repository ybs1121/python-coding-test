nums = list(map(int, input()))

answer = nums[0]

for i in range(1, len(nums)):

   if answer == 0 or answer == 1 or nums[i] == 0 or nums[i] == 1:
       answer += nums[i]
   else:
       answer *= nums[i]


print(answer)