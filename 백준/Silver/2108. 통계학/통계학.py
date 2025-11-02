import sys

input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

# 산술평균
print(int(round(sum(numbers) / n, 0)))

# 중앙값
print(numbers[n // 2])

# 최빈값
count_dict = {}

for number in numbers:
    count_dict[number] = count_dict.get(number, 0) + 1

max_count = max(count_dict.values())
candidate = []

for key, value in count_dict.items():
    if count_dict.get(key, 0) == max_count:
        candidate.append(key)

if len(candidate) >= 2:
    print(candidate[1])
else:
    print(candidate[0])

# 범위
print(max(numbers) - min(numbers))
