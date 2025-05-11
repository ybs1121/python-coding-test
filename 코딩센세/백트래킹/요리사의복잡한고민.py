# 19942
import sys

N = int(input())

min_ingre = list(map(int, input().split()))

ingre = [list(map(int, input().split())) for _ in range(N)]

answer = sys.maxsize


def recur(idx, a, b, c, d, cost):
    global answer

    if idx == N:
        if a >= min_ingre[0] and b >= min_ingre[1] and c >= min_ingre[2] and d >= min_ingre[3]:
            answer = min(answer, cost)
        return

        # 사용 했을 떄 안했을 떄
    recur(idx + 1, a + ingre[idx][0], b + ingre[idx][1],
          c + ingre[idx][2], d + ingre[idx][3], cost + ingre[idx][4])

    recur(idx + 1, a, b, c, d, cost)


recur(0, 0, 0, 0, 0, 0)

print(answer)
