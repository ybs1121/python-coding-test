import sys

input = sys.stdin.readline

N, M = map(int, input().split())

answer = []


def finder(kind, idx):
    global N, M

    if len(kind) == M:
        answer.append(kind)
        return

    for i in range(idx + 1, N + 1):
        kind.append(i)
        finder(kind + [], i)
        kind.pop()


for i in range(1, N + 1):
    finder([i], i)

answer.sort()
for i in answer:
    print(*i)
