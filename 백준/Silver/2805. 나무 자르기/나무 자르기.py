import sys

input = sys.stdin.readline

N, K = map(int, input().split())

trees = list(map(int, input().split()))

start = 1
end = max(trees)
answer = 0
while start <= end:
    mid = (start + end) // 2

    tree_sum = 0
    for tree in trees:
        cutting = tree - mid
        if cutting < 0:
            cutting = 0

        tree_sum += cutting

    if tree_sum >= K:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
