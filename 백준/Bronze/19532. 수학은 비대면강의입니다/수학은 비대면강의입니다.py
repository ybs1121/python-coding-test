nums = list(map(int, input().split()))

# 2000*2000 = 4_000_000
answer_x = -1000
answer_y = -1000
find = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (x * nums[0] + y * nums[1]) == nums[2] and (x * nums[3] + y * nums[4]) == nums[5]:
            answer_x = x
            answer_y = y
            find = True
            break  # 답을 찾으면 바로 종료
    if find:
        break

print(answer_x, answer_y)
