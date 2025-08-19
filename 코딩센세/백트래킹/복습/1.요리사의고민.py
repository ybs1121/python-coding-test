def recur(idx, dan, zzan, use):
    global answer
    if idx == N:
        if use == 0:
            return
        result = abs(zzan - dan)
        answer = min(result, answer)
        return
    recur(idx + 1, dan + ingre[idx][0], zzan * ingre[idx][1], use + 1)  # 재료 사용하는 경우
    recur(idx, dan, zzan, use)  # 재료 사용하지 않는 경우


N = int(input())
ingre = [list(map(int, input().split())) for _ in range(N)]
answer = 9999999999
recur(0, 0, 1, 0)
