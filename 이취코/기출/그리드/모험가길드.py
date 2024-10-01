n = int(input())
adventurers = list(map(int, input().split()))

adventurers.sort()

idx = 0
count = 0
while True:

    fear = adventurers[idx]

    if fear + idx > n - 1:
        break
    else:
        idx += fear
        count += 1

print(count)

