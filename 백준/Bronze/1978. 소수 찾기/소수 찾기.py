n = int(input())
nums = list(map(int, input().split()))

answer = 0

for num in nums:
    if num == 1 or num == 0:
        continue
    if num == 2:
        answer += 1
        continue
    else:
        flag = True
    if num % 2 == 0:
        continue
    else:
        flag = True
        for i in range(3, num):
            if num % i == 0:
                flag = False
                break
        if flag:
            answer += 1

print(answer)
