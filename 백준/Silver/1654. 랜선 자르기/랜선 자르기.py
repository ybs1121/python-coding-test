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

    cutting = 0

    for line in lines:
        cutting += line // mid

    if cutting >= N:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
