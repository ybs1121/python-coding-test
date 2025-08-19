import sys

N = int(input())

less = list(map(int, input().split()))

ingre = [list(map(int, input().split())) for _ in range(N)]


def recur(idx, a, b, c, d, e):
    global answer
    if idx == N:
        if a >= less[0] and b >= less[1] and c >= less[2] and d >= less[3]:
            answer = min(answer, e)
            return

    recur(idx + 1, a + ingre[idx][0], b + ingre[idx][1], c + ingre[idx][2], d + ingre[idx][3], e + ingre[idx][4])
    recur(idx + 1, a, b, c, d, e)


answer = sys.maxsize
recur(0, 0, 0, 0, 0, 0)

print(answer)
