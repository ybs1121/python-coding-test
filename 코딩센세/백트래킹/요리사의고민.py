# 2961

def recur(idx, dan, zzan, use):
    global answer

    if idx == N:
        if use == 0:
            return
        result = abs(dan - zzan)
        answer = min(answer, result)
        return

    recur(idx + 1, dan + ingre[idx][0], zzan * ingre[idx][1], use + 1)

    recur(idx + 1, dan, zzan, use)


N = int(input())
ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 999999999999

recur(0, 0, 1, 0)

print(answer)