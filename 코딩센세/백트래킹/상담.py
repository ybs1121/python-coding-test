# 14501

N = int(input())

counsels = [list(map(int, input().split())) for _ in range(N)]

answer = -1


def recur(idx, money):
    global answer

    if idx < N:
        answer = max(money, answer)
    elif idx >= N:
        return

    recur(idx + counsels[idx][0], money + counsels[idx][1])

    recur(idx + 1, money)


recur(0, 0)
print(answer)
