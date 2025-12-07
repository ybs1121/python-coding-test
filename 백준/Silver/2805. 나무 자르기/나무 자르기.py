import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

answer = 0

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for tree in trees:
        if tree > mid:
            tmp += (tree - mid)

    if tmp >= M:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
