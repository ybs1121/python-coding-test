import operator

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers.sort()

avg = round((sum(numbers) / n))

mid = numbers[n // 2]

ranges = max(numbers) - min(numbers)

count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] = count_dict[num] + 1
    else:
        count_dict[num] = 1

max_count = max(count_dict.values())

most_common_nums = []
for num, count in count_dict.items():
    if count == max_count:
        most_common_nums.append(num)

most_common_nums.sort()

if len(most_common_nums) >= 2:
    many = most_common_nums[1]
else:
    many = most_common_nums[0]

print(avg)
print(mid)
print(many)
print(ranges)
