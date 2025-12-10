import sys

input = sys.stdin.readline

N, M = map(int, input().split())

answer = []


def finder(kinds):
    global N, M
    if len(kinds) == M:
        answer.append(kinds)
        return

    for i in range(1, N + 1):
        if len(kinds) != 0 and kinds[-1] > i:
            continue
        kinds.append(i)
        finder(kinds + [])
        kinds.pop()

finder([])

answer.sort()
for a in answer:
    print(*a)
