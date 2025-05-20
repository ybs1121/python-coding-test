import sys

N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

st = 0
ed = max(trees)
answer = sys.maxsize
while st <= ed:
    mid = (st + ed) // 2

    temp = 0
    for t in trees:
        if mid <= t:
            temp += (t - mid)

    if temp >= M:
        answer = min(answer, temp)
        st = mid + 1
    else:
        ed = mid - 1
