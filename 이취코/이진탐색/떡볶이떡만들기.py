# input
# 4 6
# 19 15 10 17

n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

rice_cakes.sort()

start = 0
end = rice_cakes[-1]
answer = 0
while start <= end:

    mid = (start + end) // 2

    cutting_rice_cake = 0

    for rice_cake in rice_cakes:
        if rice_cake > mid:
            cutting_rice_cake += (rice_cake - mid)
    # print(cutting_rice_cake)
    if cutting_rice_cake >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
    # print(answer)

print(answer)
