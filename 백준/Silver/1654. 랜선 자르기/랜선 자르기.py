import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lines = []

for _ in range(K):
    lines.append(int(input()))

start = 1
end = max(lines)

answer = 0

while start <= end:
    mid = (start + end) // 2

    tmp = 0

    for line in lines:
        tmp += line // mid

    if tmp >= N:
        start = mid + 1
        answer = max(answer, mid)
    else:
        end = mid - 1

print(answer)