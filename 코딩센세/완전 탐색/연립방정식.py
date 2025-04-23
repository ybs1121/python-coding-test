# 19532

nums = list(map(int, input().split()))


for x in range(-10_000, 10_001):
    for y in range(-10_000, 10_001):
        a = nums[0]
        b = nums[1]
        c = nums[2]
        d = nums[3]
        e = nums[4]
        f = nums[5]

        if (a * x + b * y == c) and (d * x + e * y == f):
            print(x, y)
            break
