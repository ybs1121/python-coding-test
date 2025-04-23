n, m = map(int, input().split())

lectures = list(map(int, input().split()))

# lectures.sort()
start = max(lectures)
end = sum(lectures)

answer = -1

while start <= end:
    total = 0
    cnt = 0
    mid = (start + end) // 2

    for lecture in lectures:
        if total + lecture > mid:
            cnt += 1
            total = 0
        total += lecture

    if total > 0:
        cnt += 1

    if cnt > m:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)
