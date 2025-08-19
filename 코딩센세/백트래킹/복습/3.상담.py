import sys

N = int(input())

works = [list(map(int, input().split())) for _ in range(N)]


def recur(idx, amt):
    global answer

    if idx == N - 1:
        answer = max(answer, amt)
        return
    if idx > N - 1:
        return

    recur(idx + 1, amt)
    recur(idx + works[idx][0], amt + works[idx][1])


answer = sys.maxsize * - 1

recur(0, 0)
print(answer)
