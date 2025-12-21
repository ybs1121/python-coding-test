import sys

input = sys.stdin.readline

N, M = map(int, input().split())

maps = []
for i in range(N):
    maps.append(list(map(str, input().split())))

chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == "2":
            chickens.append([i, j])
        if maps[i][j] == "1":
            houses.append([i, j])

answer = sys.maxsize

visited = [False] * len(chickens)


def finder(idx, cnt):
    global answer, N, M

    if cnt == M:
        tmp_sum = 0
        for house in houses:
            tmp = sys.maxsize
            for i in range(len(chickens)):
                if visited[i]:
                    tmp = min(tmp, abs(chickens[i][0] - house[0]) + abs(chickens[i][1] - house[1]))
            tmp_sum += tmp
        answer = min(answer, tmp_sum)

    for ch in range(idx, len(chickens)):
        if not visited[ch]:
            visited[ch] = True
            finder(ch + 1, cnt + 1)
            visited[ch] = False

    return


finder(0, 0)
print(answer)
