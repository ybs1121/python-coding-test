import sys

A, B = map(int, input().split())

things = [list(map(int, input().split())) for _ in range(A)]

answer = sys.maxsize * - 1


def recur(idx, wight, value):
    global answer

    if idx == A - 1:
        if wight <= B:
            answer = max(answer, value)
        return

    recur(idx + 1, wight, value)
    recur(idx + 1, wight + things[idx][0], value + things[idx][1])


recur(0, 0, 0)
print(answer)
