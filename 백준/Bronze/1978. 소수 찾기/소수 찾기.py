import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

answer = 0


for num in numbers:
    if num == 0 or num == 1:
        continue
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        answer += 1

print(answer)

