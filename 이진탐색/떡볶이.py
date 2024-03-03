n, m = map(int, input().split())
dduck = list(map(int, input().split()))

start = 0
end = max(dduck)

print(start, end, sep=" ")
result = -1

while start <= end:
    mid = (start + end) // 2

    cut_sum = 0
    for i in dduck:
        cut_dduck = i - mid
        if cut_dduck > 0:
            cut_sum += cut_dduck

    if cut_sum == m:
        result = mid
        break

    if cut_sum > m:
        start = mid + 1
        result = mid

    elif cut_sum < m:
        end = mid - 1

print(result)
