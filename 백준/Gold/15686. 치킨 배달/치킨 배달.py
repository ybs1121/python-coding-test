import sys

input = sys.stdin.readline

N, M = map(int, input().split())

maps = []

for i in range(N):
    maps.append(list(map(int, input().split())))

chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            houses.append([i, j])
        if maps[i][j] == 2:
            chickens.append([i, j])

answer = sys.maxsize

visited = [0 for _ in range(len(chickens))]


def finder(chicken_cnt, idx):
    global N, M, answer

    if chicken_cnt == M:

        summary = 0

        for house in houses:
            chicken_dist = sys.maxsize
            for i in range(len(visited)):
                if visited[i] == 1:
                    tmp_dist = abs(chickens[i][0] - house[0]) + abs(chickens[i][1] - house[1])
                    chicken_dist = min(chicken_dist, tmp_dist)
            summary += chicken_dist

        answer = min(answer, summary)

        return

    for i in range(idx, len(chickens)):
        if visited[i] == 0:
            visited[i] = 1
            finder(chicken_cnt + 1, i + 1)
            visited[i] = 0


finder(0, 0)
print(answer)
