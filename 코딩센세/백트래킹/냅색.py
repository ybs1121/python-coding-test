# 12865

A, B = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(A)]

answer = -1


def recur(idx, w, v):
    global answer
    if idx == A:
        if w <= B:
            answer = max(answer, v)

        return

    recur(idx + 1, w + items[idx][0], v + items[idx][1])
    recur(idx + 1, w, v)


recur(0, 0, 0)
print(answer)
